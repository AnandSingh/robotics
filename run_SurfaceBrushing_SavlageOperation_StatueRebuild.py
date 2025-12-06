from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")
    # arm.move_left(300)
    # arm.move_right(300)
    # arm.move_right_time(300)

    # arm.move_left_time(40)

    # robo.pivot_turn(-76)

    robo.drive(-580)
    robo.pivot_turn(-91)

    arm.move_left(124)

    robo.pivot_turn(51)
    robo.pivot_turn(-151)
    arm.move_left(-124)
    robo.drive(-570)
    robo.pivot_turn(-67)
    robo.drive(-30)
    robo.pivot_turn(-10)
    robo.drive(85)
    robo.pivot_turn(16)
    robo.drive(-80)
    arm.move_right(-267)
    robo.set_speed_percentage(speed_percentage=50)
    robo.drive(65)
    arm.move_right(267)
    robo.pivot_turn(-85)
    robo.drive(-70)
    robo.pivot_turn(80)
    robo.drive(-260)
    robo.drive(200)
    robo.pivot_turn(-15)
    robo.drive(-300)
    arm.move_left
    """
    robo.pivot_turn(-90)
    robo.drive(100)
    """
    """
    robo.drive(-100)
    robo.drive(150)
    robo.pivot_turn(-17)
    robo.drive(-200)
    """
    """
    arm.move_left(-307)
    arm.move_right(190)
    arm.move_right(-
    170)
    robo.drive(-80)
    robo.pivot_turn(-60)
    robo.drive(-660)
    """


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
