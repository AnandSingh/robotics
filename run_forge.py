from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.set_speed_percentage(speed_percentage=50)

    robo.drive(-600)
    robo.pivot_turn(-12)
    robo.drive(-80)
    arm.move_left(100)
    robo.pivot_turn(12)
    robo.drive(20)
    robo.pivot_turn(10)
    arm.move_left(-130)
    robo.drive(700)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
