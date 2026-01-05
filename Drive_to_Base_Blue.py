from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")

    robo.set_speed_percentage(speed_percentage=100)
    robo.drive(-300)
    robo.pivot_turn(85)
    robo.drive(-1500)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
