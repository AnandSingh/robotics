from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")
    robo.set_speed_percentage(speed_percentage=70)
    # arm.move_right(120)
    robo.drive(-635)
    arm.move_right(135)
    robo.pivot_turn(-30)
    arm.move_right(-5)
    robo.drive(-65)
    arm.move_left(-30)
    # robo.pivot_turn(-5)
    robo.drive(20)
    arm.move_right(30)
    robo.set_speed_percentage(speed_percentage=30)

    robo.drive(-30)
    # arm.move_right(60)
    arm.move_right(-110)
    arm.move_left(30)
    robo.set_speed_percentage(speed_percentage=50)
    # arm.move_right(-10)
    # arm.move_right(-10)
    robo.drive(150)
    robo.pivot_turn(88)
    robo.drive(-230)

    arm.move_left(310, speed_percentage=35)
    # arm.move_left(-310)
    robo.set_speed_percentage(speed_percentage=100)
    robo.drive(200)
    robo.pivot_turn(-50)
    robo.drive(570)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
