from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Button, Icon
from pybricks.tools import wait

from NexusDrive import NexusDrive
from NexusAttachement import NexusAttachement
from run_forge import run_mission as forge_mission

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

# Color to mission mapping
COLOR_MISSIONS = {
    Color.MY_GREY: "map_reveal",
    Color.MY_BLACK: "forge",
    Color.MY_YELLOW: "whats_on_sale",
    Color.MY_WHITE: "statue_rebuild",
    Color.MY_RED: "surface_brushing",
}


def set_detectable_colors(sensor):
    """Configure the sensor to detect our custom colors."""
    my_colors = (
        Color.MY_GREY,
        Color.MY_BLACK,
        Color.MY_YELLOW,
        Color.MY_WHITE,
        Color.MY_RED,
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
        print("WHITE - Statue Rebuild")
    elif color == Color.MY_RED:
        hub.display.icon(Icon.ARROW_LEFT)
        print("RED - Surface Brushing")
    else:
        hub.display.icon(Icon.QUESTION_MARK)
        print("Unknown attachment")


def run_map_reveal(robo, arm):
    """Run the Map Reveal mission."""
    print("Running MAP REVEAL mission")
    # TODO: Add mission logic
    pass


def run_whats_on_sale(robo, arm):
    """Run the What's on Sale mission."""
    print("Running WHAT'S ON SALE mission")
    # TODO: Add mission logic
    pass


def run_forge_mission(robo, arm):
    """Run the Forge mission."""
    print("Running FORGE mission")
    # Call the existing forge mission function
    forge_mission(robo, arm)


def run_statue_rebuild(robo, arm):
    """Run the Statue Rebuild mission."""
    print("Running STATUE REBUILD mission")
    # TODO: Add mission logic
    pass


def run_surface_brushing(robo, arm):
    """Run the Surface Brushing mission."""
    print("Running SURFACE BRUSHING mission")
    # TODO: Add mission logic
    pass


# Mission dispatcher
MISSION_RUNNERS = {
    "map_reveal": run_map_reveal,
    "forge": run_forge_mission,
    "whats_on_sale": run_whats_on_sale,
    "statue_rebuild": run_statue_rebuild,
    "surface_brushing": run_surface_brushing,
}


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
        if Button.RIGHT in pressed and color == Color.MY_GREY:
            run_map_reveal(robo, arm)

        if Button.RIGHT in pressed and color == Color.MY_BLACK:
            run_forge_mission(robo, arm)

        if Button.RIGHT in pressed and color == Color.MY_YELLOW:
            run_whats_on_sale(robo, arm)

        if Button.RIGHT in pressed and color == Color.MY_WHITE:
            run_statue_rebuild(robo, arm)

        if Button.RIGHT in pressed and color == Color.MY_RED:
            run_surface_brushing(robo, arm)

        # Stop motors after mission
        robo.brake()


if __name__ == "__main__":
    main()
