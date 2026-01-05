from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    # robo.straight_drive(100)
    print("test")

    robo.drive(-40)
    robo.pivot_turn(55)
    robo.drive(-500)
    robo.pivot_turn(-18)
    robo.drive(-30)
    arm.move_left(-500)
    wait(30)
    arm.move_left(500)
    robo.drive(150)
    robo.pivot_turn(40)
    robo.drive(-350)
    robo.pivot_turn(10)
    """
    robo.pivot_turn(30)
    robo.drive(-350)
    robo.pivot_turn(-25)
    robo.drive(-300)
    """


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
