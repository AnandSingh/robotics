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
    arm.move_right(100)
    robo.pivot_turn(55)
    robo.drive(-330)
    robo.pivot_turn(110)

    robo.drive(-160)
    arm.move_left(150)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    arm.move_left(200)
    arm.move_left(-200)
    robo.drive(100)
    robo.pivot_turn(75)
    robo.drive(-550)
    robo.pivot_turn(-30)
    robo.drive(-300)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
