import BlynkLib
import RPi.GPIO as GPIO
import time

BLYNK_AUTH = 'Your_Blynk_Auth_Token'  # Replace with your Blynk Auth Token

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(17, GPIO.OUT)  # Set pin 17 to be an output pin

# Handler for writing to virtual pin V4 to control the LED
@blynk.VIRTUAL_WRITE(4)
def my_write_handler(value):
    if int(value[0]) == 1:
        GPIO.output(17, GPIO.HIGH)  # Turn LED on
    else:
        GPIO.output(17, GPIO.LOW)  # Turn LED off

# Handler for reading the LED state and sending it to virtual pin V5
@blynk.VIRTUAL_READ(5)
def my_read_handler():
    # Read the LED state
    led_state = GPIO.input(17)
    # Send LED state to virtual pin V5
    blynk.virtual_write(5, led_state)

# Add a timer to read the LED state every 1 second
timer = blynk.set_user_task(my_read_handler, 1000)  # 1000 ms = 1 second

# Start Blynk (this call should never return)
blynk.run()
