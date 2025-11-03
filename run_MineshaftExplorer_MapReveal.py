from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")

    robo.drive(-630)
    robo.pivot_turn(-30)
    arm.move_left(-50)
    arm.move_right(-3)
    robo.drive(-75)
    robo.pivot_turn(-10)
    robo.drive(17)
    arm.move_right(50)
    robo.drive(-30)
    arm.move_right(-160)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
