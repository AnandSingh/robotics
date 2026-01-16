from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.drive(-50)
    robo.pivot_turn(60)
    robo.drive(-500)
    robo.pivot_turn(-90)
    robo.drive(-50)
    arm.move_right(90)
    robo.pivot_turn(50)
    robo.drive(50)
    arm.move_right(250)
    robo.pivot_turn(55)
    robo.drive(-330)
    robo.pivot_turn(95)

    robo.drive(-160)
    arm.move_left(60)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    arm.move_left(100)
    arm.move_left(-100)
    robo.drive(100)
    robo.pivot_turn(70)
    robo.set_speed_percentage(speed_percentage=100)
    robo.drive(-900)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
