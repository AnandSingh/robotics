from NexusDrive import *
from NexusAttachement import *



def run_mission(robo, arm):
    robo.drive
    arm.move_left

    robo.drive
    robo.pivot_turn
    robo.drive
    robo.pivot_turn
    robo.drive
    robo.pivot_turn
    robo.drive
    arm.move_left
    robo.drive
    arm.move_left
    arm.move_left
    
    
    
    robo.brake()


if __name__ == "__main__":
    robo = NexusDrive()
    arm = NexusAttachement()
    run_mission(robo, arm)


