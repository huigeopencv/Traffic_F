"""Runner script for single and multiagent reinforcement learning experiments.

This script performs an RL experiment using the PPO algorithm. Choice of
hyperparameters can be seen and adjusted from the code below.

Usage
    python train_ppo.py EXP_CONFIG
"""
import argparse
import json
import sys
from copy import deepcopy

from flow.utils.rllib import FlowParamsEncoder
from flow.utils.registry import make_create_env

import os
import ray
from ray.tune import run_experiments
from ray.rllib.agents.ppo.ppo_torch_policy import  PPOTorchPolicy
# from flow.envs.multiagent.traffic_light_grid import CoTV
from Cotv_env import CoTV
from flow.networks import TrafficLightGridNetwork
from flow.core.params import SumoParams, EnvParams, InitialConfig, NetParams
from flow.core.params import InFlows, SumoCarFollowingParams, VehicleParams
from flow.controllers import GridRouter
from flow.controllers import RLController
from ray.tune.registry import register_env
from flow.utils.registry import make_create_env
from flow.core.params import TrafficLightParams
# Experiment parameters
N_ROLLOUTS = 10  # number of rollouts per training iteration
N_CPUS = 10  # number of parallel workers
HORIZON = 720  # time horizon of a single rollout
# Road network parameters
INNER_LENGTH = 300  # length of inner edges in the traffic light grid network
LONG_LENGTH = 300  # length of final edge in route
SHORT_LENGTH = 300  # length of edges that vehicles start on
# number of vehicles originating in the left, right, top, and bottom edges
N_LEFT, N_RIGHT, N_TOP, N_BOTTOM = 1, 1, 1, 1
N_ROWS = 1  # number of row of bidirectional lanes
N_COLUMNS = 1  # number of columns of bidirectional lanes
# limit vehicle driving parameters
TARGET_VELOCITY = 15  # desired velocity for all vehicles in the network, in m/s
MAX_ACCEL = 3  # maximum acceleration for autonomous vehicles, in m/s^2
MAX_DECEL = 3  # maximum deceleration for autonomous vehicles, in m/s^2
# Vehicle parameters
vehicles = VehicleParams()
vehicles.add(
    veh_id="rl",
    acceleration_controller=(RLController, {}),
    routing_controller=(GridRouter, {}),
    car_following_params=SumoCarFollowingParams(
        speed_mode="right_of_way",
        accel=MAX_ACCEL,
        decel=MAX_DECEL,
        max_speed=TARGET_VELOCITY,
    ))
# inflows of vehicles are place on all outer edges (listed here)
left_edges = ["left{}_{}".format(N_ROWS, i) for i in range(N_COLUMNS)]
right_edges = ["right0_{}".format(i) for i in range(N_COLUMNS)]
bot_edges = ["bot{}_0".format(i) for i in range(N_ROWS)]
top_edges = ["top{}_{}".format(i, N_COLUMNS) for i in range(N_ROWS)]
inflow = InFlows()
for edge in right_edges:  # S->N
    inflow.add(
        veh_type="rl",
        edge=edge,
        vehs_per_hour=120,
        begin=1,
        end=300,
        depart_lane="free",
        depart_speed="random")
for edge in bot_edges:  # W->E
    inflow.add(
        veh_type="rl",
        edge=edge,
        vehs_per_hour=240,
        begin=1,
        end=300,
        depart_lane="free",
        depart_speed="random")
for edge in left_edges:  # N->S
    inflow.add(
        veh_type="rl",
        edge=edge,
        vehs_per_hour=288,
        begin=45,
        end=345,
        depart_lane="free",
        depart_speed="random")
for edge in top_edges:  # E->W
    inflow.add(
        veh_type="rl",
        edge=edge,
        vehs_per_hour=192,
        begin=60,
        end=360,
        depart_lane="free",
        depart_speed="random")
# Integrate parameters for this module
traffic_lights=TrafficLightParams()
flow_params = dict(
    exp_tag="CoTV_1x1grid",
    env_name=CoTV,
    network=TrafficLightGridNetwork,
    simulator='traci',
    sim=SumoParams(
        restart_instance=True,
        sim_step=1,
        render=False,
        emission_path="{}output1/CoTV_1x1grid".format(os.path.abspath(os.path.dirname(__file__)).split('flow')[0]),
    ),
    env=EnvParams(
        horizon=HORIZON,
        additional_params={
            "target_velocity": TARGET_VELOCITY,
            "switch_time": 3,
            "num_observed": 1,
            "discrete": True,
            "tl_type": "controlled",
            "num_local_edges": 4,
            "num_local_lights": 4,
            "max_accel": MAX_ACCEL,
            "max_decel": MAX_DECEL,
            "safety_device": True,  # 'True' needs emission path to save output file
            "cav_penetration_rate": 1,  # used for mixed-autonomy
            "total_veh": 70,  # 240 for 1x6 grid, 70 for 1x1 grid
        },
    ),
    net=NetParams(
        inflows=inflow,
        additional_params={
            "speed_limit": TARGET_VELOCITY,
            "grid_array": {
                "short_length": SHORT_LENGTH,
                "inner_length": INNER_LENGTH,
                "long_length": LONG_LENGTH,
                "row_num": N_ROWS,#1
                "col_num": N_COLUMNS,#1
                "cars_left": N_LEFT,
                "cars_right": N_RIGHT,
                "cars_top": N_TOP,
                "cars_bot": N_BOTTOM,
            },
            "horizontal_lanes": 2,
            "vertical_lanes": 2,
        },
    ),
    veh=vehicles,
    initial=InitialConfig(
        spacing='custom',
        shuffle=True,
    ),
    tls=traffic_lights,
)

def setup_exps_rllib(flow_params,
                     n_cpus,
                     n_rollouts,
                     policy_graphs=None,
                     policy_mapping_fn=None,
                     policies_to_train=None):
    from ray import tune
    from ray.tune.registry import register_env
    try:
        from ray.rllib.agents.agent import get_agent_class
    except ImportError:
        from ray.rllib.agents.registry import get_agent_class

    horizon = flow_params['env'].horizon
    alg_run = "PPO"
    agent_cls = get_agent_class(alg_run)
    config = deepcopy(agent_cls._default_config)
    config["num_workers"] = n_cpus
    config["train_batch_size"] = horizon * n_rollouts
    config["gamma"] = 0.999  # discount rate
    config["model"].update({"fcnet_hiddens": [32, 32, 32]})
    config["use_gae"] = True
    config["lambda"] = 0.97
    config["kl_target"] = 0.02
    config["num_sgd_iter"] = 10
    config["horizon"] = horizon
    config["num_gpus"] = 1
    config["timesteps_per_iteration"] = horizon * n_rollouts
    config['no_done_at_end'] = True
    flow_json = json.dumps(
        flow_params, cls=FlowParamsEncoder, sort_keys=True, indent=4)
    config['env_config']['flow_params'] = flow_json
    config['env_config']['run'] = alg_run
    if policy_graphs is not None:
        print("policy_graphs", policy_graphs)
        config['multiagent'].update({'policies': policy_graphs})
    if policy_mapping_fn is not None:
        config['multiagent'].update(
            {'policy_mapping_fn': tune.function(policy_mapping_fn)})
    if policies_to_train is not None:
        config['multiagent'].update({'policies_to_train': policies_to_train})
    create_env, env_name = make_create_env(params=flow_params, version=0)
    # Register as rllib env
    register_env(gym_name, create_env)
    return alg_run, gym_name, config
# register_env(env_name, create_env)
create_env, env_name = make_create_env(params=flow_params, version=0)
test_env = create_env()
obs_space_tl = test_env.observation_space_tl
act_space_tl = test_env.action_space_tl
obs_space_av = test_env.observation_space_av
act_space_av = test_env.action_space_av

# Setup PG with a single policy graph for all agents
POLICY_GRAPHS = {'cav': (PPOTorchPolicy, obs_space_av, act_space_av, {}),
                 'tl': (PPOTorchPolicy, obs_space_tl, act_space_tl, {})}

def policy_mapping_fn(agent_id):
    """Map a policy in RLlib."""
    if agent_id.startswith("center"):
        return "tl"
    else:
        return "cav"
policies_to_train = ['cav', 'tl']
n_cpus = N_CPUS
n_rollouts = N_ROLLOUTS
policy_graphs = POLICY_GRAPHS

alg_run, gym_name, config = setup_exps_rllib(
        flow_params, n_cpus, n_rollouts,
        policy_graphs, policy_mapping_fn, policies_to_train)

ray.init(num_cpus=n_cpus + 1)  # , object_store_memory=200 * 1024 * 1024
exp_config = {
        "run": alg_run,
        "env": gym_name,
        "config": {
            **config
        },
        "checkpoint_freq": 30,
        "checkpoint_at_end": True,
        "max_failures": 999,
        "stop": {
            "training_iteration": 500,
        },
    }

run_experiments({flow_params["exp_tag"]: exp_config})


