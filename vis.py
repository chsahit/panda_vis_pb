from __future__ import annotations

import pickle

import tiny_tamp.pb_utils as pbu
from tiny_tamp.structs import (
    DEFAULT_JOINT_POSITIONS,
    TABLE_POSE,
    ObjectState,
    Sequence,
    SimulatorInstance,
    Trajectory,
    WorldBelief,
)


def dummy_perception() -> WorldBelief:
    box_size = 0.05

    object1 = ObjectState(
        create_object=lambda client: pbu.create_box(
            w=box_size, l=box_size, h=box_size, color=pbu.RED, client=client
        ),
        pose=pbu.multiply(pbu.Pose(pbu.Point(y=0.1, z=box_size)), TABLE_POSE),
        category="red_box",
    )

    object_states = [object1]

    return WorldBelief(object_states=object_states, robot_state=DEFAULT_JOINT_POSITIONS)


def main():
    belief = dummy_perception()

    sim_instance = SimulatorInstance.from_belief(
        belief, gui=True, real_robot=False
    )

    pbu.wait_if_gui("Press enter to start visualization", client=sim_instance.client)

    with open("traj.pkl", "rb") as f:
        path = pickle.load(f)
    joints = (0, 1, 2, 3, 4, 5, 6)
    plan = Sequence([Trajectory(0, joints, path)])
    sim_instance.execute_command(plan)


if __name__ == "__main__":
    main()
