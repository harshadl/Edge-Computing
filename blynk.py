"""
This Code is to understand DHT11 with Blynk 2.0

"""

import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
#BLYNK_AUTH_TOKEN = 'kt85ldXRL362juNQiymMClUUxdsuygTN'
BLYNK_AUTH_TOKEN = 'LT3XxNnKnHArboNHZxTp8OPATkGwnEWn'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Create BlynkTimer Instance
timer = BlynkTimer()


# function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Hi, You have Connected to New Blynk2.0")
    print(".......................................................")
    print("................... MITADT Edge Computing Lab............")
    time.sleep(2);

# Functon for collect data from sensor & send it to Server
def myData():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");

    blynk.virtual_write(0, humidity,)
    blynk.virtual_write(1, temperature)
    print("Values sent to New Blynk Server!")

timer.set_interval(2, myData)


while True:
    blynk.run()
    timer.run()
