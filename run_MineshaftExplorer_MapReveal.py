from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")
    robo.set_speed_percentage(speed_percentage=50)
    arm.move_right(120)
    robo.drive(-630)
    robo.pivot_turn(-30)
    arm.move_right(-3)
    robo.drive(-75)
    robo.pivot_turn(-5)
    robo.drive(7)
    arm.move_right(60)
    robo.drive(17)
    robo.drive(-30)
    arm.move_right(-150)
    arm.move_right(-10)
    arm.move_right(-10)
    robo.drive(150)
    robo.pivot_turn(90)
    robo.drive(-80)
    robo.pivot_turn(12)
    robo.drive(-75)
    robo.set_speed_percentage(speed_percentage=10)
    arm.move_left(270)
    robo.set_speed_percentage(speed_percentage=50)
    robo.drive(200)
    robo.pivot_turn(-50)
    robo.drive(590)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
