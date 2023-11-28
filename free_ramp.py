from flow.networks import MergeNetwork
from flow.networks import BottleneckNetwork
from flow.envs import AccelEnv as myEnv
from flow.envs.test import TestEnv
from flow.envs.merge import MergePOEnv
# from flow.envs.multiagent import MultiAgentHighwayPOEnv, MultiAgentMergePOEnv
from free_ramp_env1 import MultiAgentHighwayPOEnv
from bottleneck_env_1 import MergePOEnv
from bottleneck_env import BottleneckAccelEnv, BottleneckDesiredVelocityEnv
import json
import ray
from ray.rllib.utils.seed import seed
from ray.rllib.agents.registry import get_agent_class
# get_trainer_class
from ray.rllib.agents.callbacks import DefaultCallbacks
from ray.tune import run_experiments
from ray.tune.registry import register_env
from flow.utils.registry import make_create_env
from flow.utils.rllib import FlowParamsEncoder
from flow.controllers import IDMController, ContinuousRouter, RLController,SimLaneChangeController,StaticLaneChanger
from flow.core.experiment import Experiment
from flow.core.params import NetParams, EnvParams, InitialConfig, InFlows, \
                             VehicleParams, SumoParams, SumoCarFollowingParams, TrafficLightParams, \
                            SumoLaneChangeParams
initial_config = InitialConfig(spacing="uniform",perturbation=1, bunching=20,) # 车辆位置的初始化
seed(42, 42, 42)
# time horizon of a single rollout
HORIZON = 1500
# number of rollouts per training iteration
# N_ROLLOUTS = 20
# 为了学习率改为10，SGD改为10，warmup_steps改为70
N_ROLLOUTS = 10

# number of parallel workers
N_CPUS = 10
ADDITIONAL_NET_PARAMS = {
    # the factor multiplying number of lanes.
    "scaling": 1,
    # edge speed limit
    'speed_limit': 30
}
# ADDITIONAL_ENV_PARAMS = {
#     # maximum acceleration for autonomous vehicles, in m/s^2
#     "max_accel": 4,
#     # maximum deceleration for autonomous vehicles, in m/s^2
#     "max_decel": 7.5,
#     # desired velocity for all vehicles in the network, in m/s
#     "target_velocity": 30,
#     # maximum number of controllable vehicles in the network
#     # "num_rl": 200,
# }
ADDITIONAL_ENV_PARAMS = {
    # maximum acceleration for autonomous vehicles, in m/s^2
    "max_accel": 4,
    # maximum deceleration for autonomous vehicles, in m/s^2
    "max_decel": 7.5,
    # lane change duration for autonomous vehicles, in s. Autonomous vehicles
    # reject new lane changing commands for this duration after successfully
    # changing lanes.
    "lane_change_duration": 5,
    # whether the toll booth should be active
    "disable_tb": True,
    # whether the ramp meter is active
    "disable_ramp_metering": True,
    # velocity to use in reward functions
    "target_velocity": 30,
    # if an RL vehicle exits, place it back at the front
    "add_rl_if_exit": True,
    "num_rl": 250,
    'seed': 42,

}

class MyCallbacks(DefaultCallbacks):
    pass
def get_my_callbacks():
    return MyCallbacks()

vehicles = VehicleParams()
vehicles.add("human",
             acceleration_controller=(IDMController, {}),
             lane_change_controller=(SimLaneChangeController, {}),
             # lane_change_params=SumoLaneChangeParams(lane_change_mode=1621,),
             car_following_params=SumoCarFollowingParams(speed_mode="right_of_way",accel=4,decel=7.5,tau=1.5),
             )
vehicles.add("rl",
             acceleration_controller=(RLController, {}),
             lane_change_controller=(SimLaneChangeController, {}),
             # lane_change_params=SumoLaneChangeParams(lane_change_mode=1621, ),
             car_following_params=SumoCarFollowingParams(speed_mode="right_of_way",accel=4,decel=7.5,min_gap=1.0,sigma=0,impatience=0,tau=0.5),
             )
inflows = InFlows()
inflows.add(veh_type="human",
            edge="1",
            vehs_per_hour=1200,
            depart_lane="random",
            depart_speed="random",
            color="white",
            end="300"
            )
inflows.add(veh_type="rl",
            edge="1",
            vehs_per_hour=1800,
            depart_lane="random",
            depart_speed="random",
            color="red",
            end="300")
env_params = EnvParams(horizon=HORIZON, warmup_steps=70, clip_actions=False, additional_params=ADDITIONAL_ENV_PARAMS)
net_params = NetParams(inflows=inflows, additional_params=ADDITIONAL_NET_PARAMS)
sim_params = SumoParams(sim_step=0.2, render=False, save_render=True, restart_instance=True, emission_path='data')
traffic_lights = TrafficLightParams()
flow_params = dict(
    exp_tag="bottleneck",
    # env_name=MergePOEnv,
    env_name=MultiAgentHighwayPOEnv,
    network=BottleneckNetwork,
    simulator='traci',
    sim=sim_params,
    env=env_params,
    net=net_params,
    veh=vehicles,
    initial=initial_config,
    # tls=traffic_lights,
)
# (pid=2336956) sampler.py:591 -- More than 2006 observations for 173 env steps are buffered in the sampler.
# If this is more than you expected, check that that you set a horizon on your environment correctly and that it terminates at some point.
# Note: In multi-agent environments, `rollout_fragment_length` sets the batch size based on environment steps,
# not the steps of individual agents, which can result in unexpectedly large batches.
# Also, you may be in evaluation waiting for your Env to terminate (batch_mode=`complete_episodes`). Make sure it does at some point.
#
# (pid=2336960) ppo.py: 111 - - The magnitude of your environment rewards are more than 5334.0 x the scale of `vf_clip_param`.
# This means that it will take more than 5 34.0 iterations
# for your value function to converge.If this is not intended, consider increasing `vf_clip_param`.


def setup_exps():
    """Return the relevant components of an RLlib experiment.
    返回 RLlib 实验的相关组件。
    Returns
    -------
    str
        name of the training algorithm
    str
        name of the gym environment to be trained
    dict
        training configuration parameters
    """
    alg_run = "PPO"
    # agent_cls = get_trainer_class(alg_run)
    agent_cls = get_agent_class(alg_run)
    config = agent_cls._default_config.copy()
    config["num_workers"] = N_CPUS
    config["train_batch_size"] = HORIZON * N_ROLLOUTS
    config["gamma"] = 0.99  # discount rate
    # 全连接
    config["model"].update({"fcnet_hiddens": [24, 24]})
    config["use_gae"] = True
    config["lr"] = 1e-5
    config["lambda"] = 0.97
    config["kl_target"] = 0.02
    config["num_sgd_iter"] = 10
    config['clip_actions'] = False  # FIXME(ev) temporary ray bug
    config["horizon"] = HORIZON
    config["num_gpus"] = 1
    config["seed"] = 42
    config["framework"] = "torch"
    # config["vf_clip_param"] = 300
    # config["rollout_fragment_length"] = auto
    # config["callbacks"] = DefaultCallbacks
    # config["num_envs_per_worker"] =

    # save the flow params for replay
    flow_json = json.dumps(
        flow_params, cls=FlowParamsEncoder, sort_keys=True, indent=4)
    config['env_config']['flow_params'] = flow_json
    config['env_config']['run'] = alg_run
    # config['multiagent'] = 
    create_env, gym_name = make_create_env(params=flow_params, version=0)
    # Register as rllib env
    register_env(gym_name, create_env)
    return alg_run, gym_name, config
alg_run, gym_name, config = setup_exps()

ray.init(num_cpus=N_CPUS + 1)
trials = run_experiments({
    flow_params["exp_tag"]: {
        "run": alg_run,
        "env": gym_name,
        "config": {**config},
        "checkpoint_freq": 30,
        "checkpoint_at_end": True,
        "max_failures": 999,
        "stop": {"training_iteration": 1000, },
    }
})








