from NexusDrive import *
from NexusAttachement import *


async def run_mission(robo, arm):
    print("test")
    await multitask(arm.move_left_async(20), arm.move_right_async(20))


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_task(run_mission(robo, arm))
