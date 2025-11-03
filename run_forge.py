from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.set_speed_percentage(speed_percentage=50)

    robo.brake()

    robo.drive(-560)
    robo.pivot_turn(40)
    robo.drive(-75)
    robo.pivot_turn(-35)
    robo.drive(-20)
    robo.drive(100)
    robo.pivot_turn(-30)
    robo.drive(400)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
