from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BCM)

led1 = 6
led2 = 24
led3 = 5
led4 = 12

sw1 = 26
sw2 = 19
sw3 = 16
sw4 = 18

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set input pin and set initial value to be pulled low (off)
GPIO.setup(sw2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



while True:
    
    if GPIO.input(sw1) == GPIO.HIGH:
        sleep(0.5)
        GPIO.output(led1, GPIO.HIGH)
    
    elif GPIO.input(sw2) == GPIO.HIGH:
        sleep(0.5)
        GPIO.output(led2, GPIO.HIGH)


    elif GPIO.input(sw3) == GPIO.HIGH:
        sleep(0.5)
        GPIO.output(led3, GPIO.HIGH)

    elif GPIO.input(sw4) == GPIO.HIGH:
        sleep(0.5)
        GPIO.output(led4, GPIO.HIGH)
    
    else:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)


