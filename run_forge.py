from NexusDrive import *
from NexusAttachement import *


def run_mission(robo, arm):
    robo.set_speed_percentage(speed_percentage=50)

    robo.brake()

    # robo.drive(-660)
    # robo.pivot_turn(30)
    # arm.move_left(60)
    # exit(0)
    # arm.move_left(60)
    # robo.pivot_turn(35)
    # robo.drive(100)
    # robo.pivot_turn(-30)
    # robo.drive(400)
    # robo.pivot_turn(90)
    # robo.drive(50)

    robo.drive(-280)
    robo.pivot_turn(-30)
    robo.drive(-250)
    robo.pivot_turn(50)
    robo.drive(-200)
    arm.move_left(-60)
    for _ in range(150):
        print("Beep!")
    robo.set_speed_percentage(turn_rate_percentage=10, turn_acceleration_percentage=1)
    robo.drive(100)
    robo.curve_turn(10, -50)
    robo.set_speed_percentage(speed_percentage=50, acceleration_percentage=25)
    robo.drive(200)
    # robo.set_speed_percentage(speed_percentage=5, acceleration_percentage=1)
    robo.curve_turn(10, -25)
    # robo.set_speed_percentage(speed_percentage=50, acceleration_percentage=25)
    robo.drive(500)

    # robo.drive(280)


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)
