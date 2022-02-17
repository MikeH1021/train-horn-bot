from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BCM)

sw1 = 26
sw2 = 19
sw3 = 16
sw4 = 18

GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(sw2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    
    if GPIO.input(sw1) == GPIO.HIGH:
        sleep(0.5)
        print("Button 1was pushed!")
    
    elif GPIO.input(sw2) == GPIO.HIGH:
        sleep(0.5)
        print("Button 2 was pushed!")

    elif GPIO.input(sw3) == GPIO.HIGH:
        sleep(0.5)
        print("Button 3 was pushed!")

    elif GPIO.input(sw4) == GPIO.HIGH:
        sleep(0.5)
        print("Button 4 was pushed!")
    
    else:
        continue
