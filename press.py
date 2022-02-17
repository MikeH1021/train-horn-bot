import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BCM)

sw1 = 16
sw2 = 18
sw3 = 19
sw4 = 26

GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(sw2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    
    if GPIO.input(sw1) == GPIO.HIGH:
        print("Button 1was pushed!")
    
    elif GPIO.input(sw2) == GPIO.HIGH:
        print("Button 2 was pushed!")

    elif GPIO.input(sw3) == GPIO.HIGH:
        print("Button 3 was pushed!")

    elif GPIO.input(sw1) == GPIO.HIGH:
        print("Button 4 was pushed!")
    
    else:
        pass
