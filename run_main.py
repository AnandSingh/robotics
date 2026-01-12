from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Button, Icon
from pybricks.tools import wait

from NexusDrive import NexusDrive
from NexusAttachement import NexusAttachement
from run_forge import run_mission as forge_mission
from run_MineshaftExplorer_MapReveal import run_mission as map_shaft_mission
from run_SurfaceBrushing_SavlageOperation_StatueRebuild import (
    run_mission as surface_operation_rebuild_mission,
)
from run_whats_on_sale import run_mission as whats_on_sale_mission
from run_StatueRebuild_old import run_mission as statue_rebuild_mission
from run_who_lived_here import run_mission as who_lived_here_mission
from run_statue_rebuild_1 import run_mission as statue_rebuild_mission_1
from cleaning_robot import clean_robot as cleaning_wheels
from Drive_to_Base_Blue import run_mission as drive_to_blue_base
from run_heavy_lifting import run_mission as heavy_lifting_mission

# Initialize the hub
hub = PrimeHub()

# Shub.system.set_stop_button(None)


# Initialize the color sensor (adjust port as needed)
front_sensor = ColorSensor(Port.B)

# Define custom colors based on HSV measurements
Color.MY_GREY = Color(h=195, s=13, v=67)  # Map Reveal
Color.MY_BLACK = Color(h=180, s=66, v=3)  # Forge
Color.MY_YELLOW = Color(h=52, s=70, v=99)  # What's on Sale
Color.MY_WHITE = Color(h=0, s=0, v=100)  # Statue Rebuild
Color.MY_RED = Color(h=353, s=87, v=67)  # Surface Brushing
Color.MY_GREEN = Color(h=158, s=68, v=17)
Color.MY_PEACH = Color(h=50, s=46, v=68)
# Color to mission mapping
COLOR_MISSIONS = {
    Color.MY_GREY: "map_reveal",
    Color.MY_BLACK: "forge",
    Color.MY_YELLOW: "whats_on_sale",
    Color.MY_WHITE: "heavy_lifting",
    Color.MY_RED: "surface_brushing",
    Color.MY_GREEN: "statue_rebuild_1",
    Color.MY_PEACH: "drive_to_blue_base",
}


def set_detectable_colors(sensor):
    """Configure the sensor to detect our custom colors."""
    my_colors = (
        Color.MY_GREY,
        Color.MY_BLACK,
        Color.MY_YELLOW,
        Color.MY_WHITE,
        Color.MY_RED,
        Color.MY_GREEN,
        Color.MY_PEACH,
    )
    sensor.detectable_colors(my_colors)


def scan_colors(sensor):
    """Debug function to scan and print HSV values."""
    while True:
        hsv = sensor.hsv(surface=True)
        color = sensor.color(surface=True)
        print("HSV:", hsv, "Color:", color)
        wait(500)


def show_icon(color):
    """Display icon on hub based on detected color."""
    if color == Color.MY_GREY:
        hub.display.icon(Icon.ARROW_LEFT)
        print("GREY - Map Reveal")
    elif color == Color.MY_BLACK:
        hub.display.icon(Icon.ARROW_LEFT)
        print("BLACK - Forge")
    elif color == Color.MY_YELLOW:
        hub.display.icon(Icon.ARROW_LEFT)
        print("YELLOW - What's on Sale")
    elif color == Color.MY_WHITE:
        hub.display.icon(Icon.ARROW_LEFT)
        print("WHITE - Heavy Lifting")
    elif color == Color.MY_RED:
        hub.display.icon(Icon.ARROW_LEFT)
        print("RED - Surface Brushing")
    elif color == Color.MY_GREEN:
        hub.display.icon(Icon.ARROW_LEFT)
        print("GREEN - Statue Rebuild 1")
    elif color == Color.MY_PEACH:
        hub.display.icon(Icon.ARROW_LEFT)
        print("TAN - Drive to blue base")
    else:
        hub.display.icon(Icon.QUESTION_MARK)
        print("Unknown attachment")


def main():
    # Initialize robot and attachment
    robo = NexusDrive()
    arm = NexusAttachement()

    # Configure detectable colors
    set_detectable_colors(front_sensor)

    # Uncomment to debug/calibrate colors:
    # scan_colors(front_sensor)

    print("Ready - Scan attachment and press button")

    # Main loop
    while True:
        # Scan the attachment color
        color = front_sensor.color()

        # Show icon for detected color
        show_icon(color)

        # Turn on hub light if color detected
        if color in COLOR_MISSIONS:
            hub.light.on(Color.GREEN)
        else:
            hub.light.off()

        wait(100)

        # Check for button press
        pressed = hub.buttons.pressed()
        # print("Pressed buttons:", pressed)

        # Run mission based on color + button
        if Button.LEFT in pressed and color == Color.MY_GREY:
            map_shaft_mission(robo, arm)

        if Button.LEFT in pressed and color == Color.MY_BLACK:
            forge_mission(robo, arm)

        if Button.LEFT in pressed and color == Color.MY_YELLOW:
            whats_on_sale_mission(robo, arm)

        if Button.LEFT in pressed and color == Color.MY_WHITE:
            heavy_lifting_mission(robo, arm)

        if Button.LEFT in pressed and color == Color.MY_RED:
            surface_operation_rebuild_mission(robo, arm)

        if Button.LEFT in pressed and color == Color.MY_GREEN:
            statue_rebuild_mission_1(robo, arm)

        if Button.LEFT in pressed and color == Color.MY_PEACH:
            drive_to_blue_base(robo, arm)

        if Button.RIGHT in pressed:
            cleaning_wheels(robo, arm)

        # Stop motors after mission
        robo.brake()


if __name__ == "__main__":
    main()
