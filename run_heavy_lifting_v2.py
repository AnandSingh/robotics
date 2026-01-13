from NexusDrive import *
from NexusAttachement import *


def get_loading(robo, arm):
    while True:
        arm.move_right(10, speed_percentage=20)
        load = arm.check_right_load()
        arm.move_right(-10, speed_percentage=20)
        print("Right Load: {}".format(load))


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
    old_load = arm.check_right_load()
    robo.drive(-30)
    arm.move_right(-120, speed_percentage=10)
    new_load = arm.check_right_load()
    robo.drive(100)
    robo.pivot_turn(-90)
    robo.drive(-150)
    robo.pivot_turn(-40)
    arm.move_left(-100)
    arm.move_left(200)

    if new_load > old_load and new_load > 50:
        print("Load increased from {} to {}".format(old_load, new_load))
        print("Heavy lifting detected!")
        robo.pivot_turn(20)
        robo.drive(-400)

    else:
        print(
            "Load did not increase significantly: {} to {}".format(old_load, new_load)
        )
        robo.pivot_turn(50)
        robo.set_speed_percentage(speed_percentage=90)
        robo.drive(720)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    # test_loading(robo, arm)
    run_mission(robo, arm)
