# # import matplotlib.pyplot as plt
# # squares = [1, 4, 9, 16, 25]
# # plt.plot(squares)
# # plt.show()
# import ray
# from ray import tune
# # from ray.rllib.algorithms.algorithm import Algorithm
#
# # Use the Algorithm's `from_checkpoint` utility to get a new algo instance
# # that has the exact same state as the old one, from which the checkpoint was
# # created in the first place:
# # my_new_ppo = Algorithm.from_checkpoint(path_to_checkpoint)
#
# # Continue training.
# # my_new_ppo.train()
# from flow.networks import MergeNetwork
# from flow.networks import BottleneckNetwork
# from flow.envs import AccelEnv as myEnv
# from flow.envs.test import TestEnv
# from flow.envs.merge import MergePOEnv
# # from flow.envs.multiagent import MultiAgentHighwayPOEnv, MultiAgentMergePOEnv
# from free_ramp_env1 import MultiAgentHighwayPOEnv
# import json
# import ray
# from ray.rllib.agents.registry import get_agent_class
# from ray.tune import run_experiments,run
# from ray.tune.registry import register_env
# from flow.utils.registry import make_create_env
# from flow.utils.rllib import FlowParamsEncoder
# from flow.controllers import IDMController, ContinuousRouter, RLController,SimLaneChangeController,StaticLaneChanger
# from flow.core.experiment import Experiment
# from flow.core.params import NetParams, EnvParams, InitialConfig, InFlows, \
#                              VehicleParams, SumoParams, SumoCarFollowingParams, TrafficLightParams, \
#                             SumoLaneChangeParams
# initial_config = InitialConfig(spacing="uniform",perturbation=1, bunching=20,) # 车辆的初始化
#
# # time horizon of a single rollout
# HORIZON = 1500
# # number of rollouts per training iteration
# N_ROLLOUTS = 20
# # number of parallel workers
# N_CPUS = 10
# ADDITIONAL_NET_PARAMS = {
#     # the factor multiplying number of lanes.
#     "scaling": 1,
#     # edge speed limit
#     'speed_limit': 30
# }
# ADDITIONAL_ENV_PARAMS = {
#     # maximum acceleration for autonomous vehicles, in m/s^2
#     "max_accel": 3,
#     # maximum deceleration for autonomous vehicles, in m/s^2
#     "max_decel": 7.5,
#     # desired velocity for all vehicles in the network, in m/s
#     "target_velocity": 30,
#     # maximum number of controllable vehicles in the network
#     # "num_rl": 200,
# }
# vehicles = VehicleParams()
# vehicles.add("human",
#              acceleration_controller=(IDMController, {}),
#              lane_change_controller=(SimLaneChangeController, {}),
#              lane_change_params=SumoLaneChangeParams(lane_change_mode=1621,),
#              car_following_params=SumoCarFollowingParams(speed_mode="obey_safe_speed"),
#              )
# vehicles.add("rl",
#              acceleration_controller=(RLController, {}),
#              lane_change_controller=(SimLaneChangeController, {}),
#              lane_change_params=SumoLaneChangeParams(lane_change_mode=1621, ),
#              car_following_params=SumoCarFollowingParams(speed_mode="obey_safe_speed"),
#              )
# inflows = InFlows()
# inflows.add(veh_type="human",
#             edge="1",
#             vehs_per_hour=1200,
#             depart_lane="random",
#             depart_speed="random",
#             color="white",
#             end="300"
#             )
# inflows.add(veh_type="rl",
#             edge="1",
#             vehs_per_hour=1200,
#             depart_lane="random",
#             depart_speed="random",
#             color="red",
#             end="300")
# env_params = EnvParams(horizon=HORIZON, warmup_steps=100, clip_actions=False, additional_params=ADDITIONAL_ENV_PARAMS)
# net_params = NetParams(inflows=inflows, additional_params=ADDITIONAL_NET_PARAMS)
# sim_params = SumoParams(sim_step=0.2, render=False, restart_instance=True, emission_path='data')
# traffic_lights = TrafficLightParams()
# flow_params = dict(
#     exp_tag="bottleneck",
#     env_name=MultiAgentHighwayPOEnv,
#     network=BottleneckNetwork,
#     simulator='traci',
#     sim=sim_params,
#     env=env_params,
#     net=net_params,
#     veh=vehicles,
#     initial=initial_config,
#     # tls=traffic_lights,
# )
# #
# # def setup_exps():
# #     """Return the relevant components of an RLlib experiment.
# #     返回 RLlib 实验的相关组件。
# #     Returns
# #     -------
# #     str
# #         name of the training algorithm
# #     str
# #         name of the gym environment to be trained
# #     dict
# #         training configuration parameters
# #     """
# #     alg_run = "PPO"
# #     agent_cls = get_agent_class(alg_run)
# #     config = agent_cls._default_config.copy()
# #     config["num_workers"] = N_CPUS
# #     config["train_batch_size"] = HORIZON * N_ROLLOUTS
# #     config["gamma"] = 0.999  # discount rate
# #     config["model"].update({"fcnet_hiddens": [3, 3]})
# #     config["use_gae"] = True
# #     config["lambda"] = 0.97
# #     config["kl_target"] = 0.02
# #     config["num_sgd_iter"] = 10
# #     config['clip_actions'] = False  # FIXME(ev) temporary ray bug
# #     config["horizon"] = HORIZON
# #     config["num_gpus"] = 1
# #     config["framework"] = "torch"
# #     # config["callbacks"] =
# #
# #     # save the flow params for replay
# #     flow_json = json.dumps(
# #         flow_params, cls=FlowParamsEncoder, sort_keys=True, indent=4)
# #     config['env_config']['flow_params'] = flow_json
# #     config['env_config']['run'] = alg_run
# #     create_env, gym_name = make_create_env(params=flow_params, version=0)
# #     # Register as rllib env
# #     register_env(gym_name, create_env)
# #     return alg_run, gym_name, config
# # alg_run, gym_name, config = setup_exps()
# #
# # ray.init(num_cpus=N_CPUS + 1)
# # # my_new_ppo = tune.run.restore='/home/jt/ray_results/bottleneck/experiment_state-2023-04-12_11-06-45.json'
# #
# # # trials = run_experiments({
# # #     flow_params["exp_tag"]: {
# # #         "run": alg_run,
# # #         "env": gym_name,
# # #         "config": {**config},
# # #         # "checkpoint_freq": 1,
# # #         # "checkpoint_at_end": True,
# # #         # "max_failures": 999,
# # #         # "stop": {"training_iteration": 1000, },
# # #         "restore":'/home/jt/ray_results/bottleneck/PPO_MultiAgentHighwayPOEnv-v0_0_2023-04-12_11-18-31nywyio_a/checkpoint_1'
# # #     },
# # # # restore='/home/jt/ray_results/bottleneck/experiment_state-2023-04-12_11-06-45.json'
# # # })
# ray.init()
# create_env, gym_name = make_create_env(params=flow_params, version=0)
#     # Register as rllib env
# register_env(gym_name, create_env)
# restore_1='/home/jt/ray_results/bottleneck/PPO_MultiAgentHighwayPOEnv-v0_0_2023-04-13_11-37-152tqwmnpa/checkpoint_1/checkpoint-1'
# from ray.rllib.agents.registry import get_agent_class
# alg_run = "PPO"
# agent_cls = get_agent_class(alg_run)
# config = agent_cls._default_config.copy()
# config["num_workers"] = N_CPUS
# config["train_batch_size"] = HORIZON * N_ROLLOUTS
# config["gamma"] = 0.999  # discount rate
# config["model"].update({"fcnet_hiddens": [3, 3]})
# config["use_gae"] = True
# config["lambda"] = 0.97
# config["kl_target"] = 0.02
# config["num_sgd_iter"] = 10
# config['clip_actions'] = False  # FIXME(ev) temporary ray bug
# config["horizon"] = HORIZON
# config["num_gpus"] = 1
# config["framework"] = "torch"
# algo = agent_cls(env=gym_name,config=config)
# checkpoint_dir = "/home/jt/flow_w/"
# for i in range(1000):
#     result = algo.train()
#     # if i % 2 == 0:
#     #     checkpoint_file = algo.save(checkpoint_dir)
#
#         # eval_result = algo.evaluate()
# algo.restore(restore_1)
# # import pickle
# # with open(restore_1 + ".tune_metadata", "rb") as f:
# #     metadata = pickle.load(f)
# # print(metadata)
#
#
import ast
import json
import yaml
path = '/home/jt/ray_results/bottleneck/PPO_MergePOEnv-v0_2365c_00000_0_2023-07-10_11-09-10/params.json'

with open(path, "r") as f:
    row_data = json.load(f)
if type(row_data) == dict:
    flow_params = json.loads(row_data['env_config']['flow_params'])
else:
    flow_params = json.load(open(row_data, 'r'))
# m=row_data['env_config']['flow_params']
print(flow_params["veh"])
print(type(flow_params))
# m=yaml.load(m,Loader=yaml.FullLoader)
# print(m)
#
# print(m["veh"])
# for veh_params in flow_params["veh"]:
#     print(veh_params)
#     print(veh_params['acceleration_controller'][0])
#     print(veh_params['acceleration_controller'][1])

# print(type(m))
# mm = ast.literal_eval(m)
# print(type(mm))
# for i in m.keys():
#     print(i)
# print(m["veh"])
# print(type(m["veh"]))
















