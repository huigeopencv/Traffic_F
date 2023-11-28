"""Script containing the Flow kernel object for interacting with simulators."""

import warnings
from flow.core.kernel.simulation import TraCISimulation, AimsunKernelSimulation
from flow.core.kernel.network import TraCIKernelNetwork, AimsunKernelNetwork
from flow.core.kernel.vehicle import TraCIVehicle, AimsunKernelVehicle
from flow.core.kernel.traffic_light import TraCITrafficLight, \
    AimsunKernelTrafficLight
from flow.utils.exceptions import FatalFlowError


class Kernel(object):
    """Kernel for abstract function calling across traffic simulator APIs.
    跨交通模拟器 API 调用抽象函数的内核。

    The kernel contains four different subclasses for distinguishing between
    the various components of a traffic simulator.
    内核包含四个不同的子类，用于区分交通模拟器的各个组件。

    * simulation: controls starting, loading, saving, advancing, and resetting
      a simulation in Flow (see flow/core/kernel/simulation/base.py)
      模拟：控制在 Flow 中开始、加载、保存、推进和重置模拟（参见 flow/core/kernel/simulation/base.py）
    * network: stores network-specific information (see
      flow/core/kernel/network/base.py)
      network：存储特定于网络的信息（参见 flow/core/kernel/network/base.py）
    * vehicle: stores and regularly updates vehicle-specific information. At
      times, this class is optimized to efficiently collect information from
      the simulator (see flow/core/kernel/vehicle/base.py).
      车辆：存储并定期更新车辆特定信息。有时，此类经过优化以有效地从模拟器收集信息（请参阅 flow/core/kernel/vehicle/base.py）。
    * traffic_light: stores and regularly updates traffic light-specific
      information (see flow/core/kernel/traffic_light/base.py).
      traffic_light：存储并定期更新交通灯特定信息（参见 flow/core/kernel/traffic_light/base.py）。

    The above kernel subclasses are designed specifically to support
    simulator-agnostic state information calling. For example, if you would
    like to collect the vehicle speed of a specific vehicle, then simply type:
    上述内核子类专门设计用于支持与模拟器无关的状态信息调用。例如，如果您想收集特定车辆的车速，则只需键入：

    >>> k = Kernel(simulator="...")  # a kernel for some simulator type
    >>> veh_id = "..."  # some vehicle ID
    >>> speed = k.vehicle.get_speed(veh_id)

    In addition, these subclasses support sending commands to the simulator via
    its API. For example, in order to assign a specific vehicle a target
    acceleration, type:
    此外，这些子类支持通过其API向模拟器发送命令。例如，要为特定车辆分配目标加速度，请键入：

    >>> k = Kernel(simulator="...")  # a kernel for some simulator type
    >>> veh_id = "..."  # some vehicle ID
    >>> k.vehicle.apply_acceleration(veh_id)

    These subclasses can be modified and recycled to support various different
    traffic simulators, e.g. SUMO, AIMSUN, TruckSim, etc...
    可以修改和回收这些子类以支持各种不同的交通模拟器，例如 SUMO、AIMSUN、TruckSim 等...
    """

    def __init__(self, simulator, sim_params):
        """Instantiate a Flow kernel object.

        Parameters
        ----------
        simulator : str
            simulator type, must be one of {"traci"}
        sim_params : flow.core.params.SimParams
            simulation-specific parameters

        Raises
        ------
        flow.utils.exceptions.FatalFlowError
            if the specified input simulator is not a valid type
            如果指定的输入模拟器不是有效类型
        """
        self.kernel_api = None

        if simulator == "traci":
            self.simulation = TraCISimulation(self)
            self.network = TraCIKernelNetwork(self, sim_params)
            self.vehicle = TraCIVehicle(self, sim_params)
            self.traffic_light = TraCITrafficLight(self)
        elif simulator == 'aimsun':
            self.simulation = AimsunKernelSimulation(self)
            self.network = AimsunKernelNetwork(self, sim_params)
            self.vehicle = AimsunKernelVehicle(self, sim_params)
            self.traffic_light = AimsunKernelTrafficLight(self)
        else:
            raise FatalFlowError('Simulator type "{}" is not valid.'.
                                 format(simulator))

    def pass_api(self, kernel_api):
        """Pass the kernel API to all kernel subclasses.将内核API传递给所有内核子类。"""
        self.kernel_api = kernel_api
        self.simulation.pass_api(kernel_api)
        self.network.pass_api(kernel_api)
        self.vehicle.pass_api(kernel_api)
        self.traffic_light.pass_api(kernel_api)

    def update(self, reset):
        """Update the kernel subclasses after a simulation step.
        在模拟步骤后更新内核子类。

        This is meant to support optimizations in the performance of some
        simulators. For example, this step allows the vehicle subclass in the
        "traci" simulator uses the ``update`` method to collect and store
        subscription information.
        这是为了支持优化某些模拟器的性能。例如，此步骤允许“traci”模拟器中的车辆子类使用``update``方法来收集和存储订阅信息。

        Parameters
        ----------
        reset : bool
            specifies whether the simulator was reset in the last simulation
            step
        """
        self.vehicle.update(reset)
        self.traffic_light.update(reset)
        self.network.update(reset)
        self.simulation.update(reset)

    def close(self):
        """Terminate all components within the simulation and network."""
        self.network.close()
        self.simulation.close()

    @property
    def scenario(self):
        """Return network for this deprecated method.此已弃用方法的返回网络。"""
        warnings.simplefilter('always', PendingDeprecationWarning)
        warnings.warn(
            "self.k.scenario will be deprecated in a future release. Please "
            "use self.k.network instead.",
            PendingDeprecationWarning
        )
        return self.network
