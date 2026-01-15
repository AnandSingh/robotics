from NexusDrive import *
from NexusAttachement import *


# alingn robot
def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")
    robo.set_speed_percentage(speed_percentage=50)
    robo.drive(-670)
    robo.pivot_turn(40)
    arm.move_left(-80)
    robo.drive(-50)
    arm.move_right(115)
    robo.drive(-30)
    arm.move_right(-120, speed_percentage=10)
    robo.drive(100)
    robo.pivot_turn(-90)
    robo.drive(-150)
    robo.pivot_turn(-40)
    arm.move_left(-100)
    arm.move_left(200)
    robo.pivot_turn(60)
    robo.set_speed_percentage(speed_percentage=90)
    robo.drive(770)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
