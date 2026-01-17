from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.set_speed_percentage(speed_percentage=50)

    robo.drive(-600)
    robo.pivot_turn(-12)
    robo.drive(-70)
    arm.move_left(100)
    robo.pivot_turn(20)
    robo.drive(15)
    robo.pivot_turn(10)
    arm.move_left(-60)
    robo.drive(50)
    robo.pivot_turn(40)
    robo.drive(-65)
    robo.drive(-250)
    robo.drive(300)
    robo.pivot_turn(-90)
    robo.set_speed_percentage(speed_percentage=100)
    robo.drive(600)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
