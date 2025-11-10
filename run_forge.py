from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.set_speed_percentage(speed_percentage=50)

    robo.brake()

    robo.drive(-660)
    robo.pivot_turn(30)
    arm.move_left(60)
    exit(0)
    arm.move_left(60)
    robo.pivot_turn(35)
    robo.drive(100)
    robo.pivot_turn(-30)
    robo.drive(400)
    robo.pivot_turn(90)
    robo.drive(50)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
