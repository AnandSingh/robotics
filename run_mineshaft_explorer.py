from NexusDrive import *
from NexusAttachement import *


# alingn robot
def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")

    robo.drive(-100)
    robo.pivot_turn(10)
    robo.drive(-300)
    robo.pivot_turn(14)
    robo.drive(-270)
    robo.pivot_turn(8.5)
    robo.drive(-80)
    arm.move_right(-200, speed_percentage=35)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
