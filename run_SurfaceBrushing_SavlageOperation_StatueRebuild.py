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

    robo.drive(-618)
    robo.pivot_turn(-150)
    robo.pivot_turn(120)
    robo.pivot_turn(-150)
    arm.move_left(100)
    robo.drive(-550)
    robo.pivot_turn(-71)
    robo.drive(-20)
    robo.pivot_turn(10)
    robo.drive(-100)
    robo.pivot_turn(-14)
    arm.move_right(-200)
    robo.drive(150)
    arm.move_right(200)
    robo.pivot_turn(-80)
    robo.drive(-100)
    robo.pivot_turn(76)
    robo.drive(-400)
    robo.drive(100)
    robo.pivot_turn(-30)
    robo.drive(550)
    """
    robo.pivot_turn(-90)
    arm.move_left(-200)

    robo.pivot_turn(-85)

    robo.drive(-590)
    robo.pivot_turn(-67)
    robo.drive(-30)
    robo.pivot_turn(-10)
    robo.drive(85)
    robo.pivot_turn(20)
    robo.drive(-62)
    arm.move_right(-267)
    robo.set_speed_percentage(speed_percentage=50)
    robo.drive(60)
    arm.move_right(267)
    robo.pivot_turn(-85)
    robo.drive(-90)
    robo.pivot_turn(80)
    robo.drive(-230)
    robo.drive(500)
    """
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

    # run_mission1(robo, arm)
    # run_mission2(robo, arm)
    run_mission(robo, arm)
