from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.set_speed_percentage(speed_percentage=75)
    robo.drive(-200)
    robo.pivot_turn(-40)
    robo.drive(-250)
    robo.set_speed_percentage(speed_percentage=25)
    robo.drive(-60)
    arm.move_left(250)
    robo.drive(100)
    arm.move_left(-200)
    robo.drive(65)
    arm.move_left(200)
    robo.pivot_turn(-20)
    robo.set_speed_percentage(speed_percentage=75)
    robo.drive(400)
    robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
