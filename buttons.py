import RPi.GPIO as GPIO
import time

led1 = 17
led2 = 24
led3 = 5
led4 = 12

sw1 = 16
sw2 = 0
sw3 = 19
sw4 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)


while True:
    #turn on leds
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led4, GPIO.HIGH)
    #turn off leds
    GPIO.output(led1, GPIO.LOW)
    time.sleep(1)
    GPIO.output(led2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(led3, GPIO.LOW)
    time.sleep(1)
    GPIO.output(led4, GPIO.LOW)
    time.sleep(1)