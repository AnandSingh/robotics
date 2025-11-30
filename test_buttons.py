from pybricks.hubs import PrimeHub  # or TechnicHub, CityHub, etc.
from pybricks.parameters import Button, Color
from pybricks.tools import wait

# Initialize the hub
hub = PrimeHub()
hub.system.set_stop_button(None)

# Simple button press detection
while True:
    # Get currently pressed buttons
    print("Checking for button presses...")
    pressed = hub.buttons.pressed()

    # Check for specific buttons
    if Button.LEFT in pressed:
        print("Left button pressed")
        hub.light.on(Color.RED)

    if Button.RIGHT in pressed:
        print("Right button pressed")
        hub.light.on(Color.BLUE)

    if Button.CENTER in pressed:
        print("Center button pressed")
        hub.light.on(Color.GREEN)

    # If no button pressed, turn off light
    if not pressed:
        hub.light.off()

    wait(100)  # Small delay to avoid flooding

#   Wait for a specific button press:

#   from pybricks.hubs import PrimeHub
#   from pybricks.parameters import Button, Color
#   from pybricks.tools import wait

#   hub = PrimeHub()

#   print("Press the center button to start...")

#   # Wait until center button is pressed
#   while Button.CENTER not in hub.buttons.pressed():
#       wait(10)

#   print("Started!")
#   hub.light.on(Color.GREEN)
