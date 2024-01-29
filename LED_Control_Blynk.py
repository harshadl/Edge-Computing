import BlynkLib
import RPi.GPIO as GPIO

BLYNK_AUTH = 'Your_Blynk_Auth_Token'  # Replace with your Blynk Auth Token

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(17, GPIO.OUT)  # Set pin 17 to be an output pin

# Register Virtual Pin
@blynk.VIRTUAL_WRITE(4)
def my_write_handler(value):
    # This function will be called every time
    # there is an update on Virtual Pin V4
    if int(value[0]) == 1:
        GPIO.output(17, GPIO.HIGH)  # Turn LED on
    else:
        GPIO.output(17, GPIO.LOW)  # Turn LED off

# Start Blynk (this call should never return)
blynk.run()
