from NexusDrive import *
from NexusAttachement import *


async def run_mission(robo, arm):
    print("test")
    robo.straight_drive(300)
    await multitask(
        robo.straight_drive_async(500),
        arm.move_left_async(200),
        arm.move_right_async(200),
    )


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_task(run_mission(robo, arm))
