from NexusDrive import *
from NexusAttachement import *


def clean_robot(robo, arm):
    while True:
        robo.drive(1000)
        robo.drive(-1000)
