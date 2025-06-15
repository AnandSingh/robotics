from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):

   
    robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
