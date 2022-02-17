import RPi.GPIO as GPIO
import time

sw1 = 16
sw2 = 18
sw3 = 19
sw4 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1, GPIO.IN)
GPIO.setup(sw2, GPIO.IN)
GPIO.setup(sw3, GPIO.IN)
GPIO.setup(sw4, GPIO.IN)

while True:
    
    if (GPIO.input(sw1)):
        print("Button 1 Pressed")
    
    elif (GPIO.input(sw2)):
        print("Button 2 Pressed")

    elif (GPIO.input(sw3)):
        print("Button 3 Pressed")

    elif (GPIO.input(sw4)):
        print("Button 4 Pressed")
    
    else:
        break
