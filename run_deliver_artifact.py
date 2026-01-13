from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")

    robo.drive(-450)
    robo.drive(450)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
