import RPi.GPIO as GPIO
import time

led = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)


GPIO.output(led, GPIO.HIGH)
print("Led turned on.")
time.sleep(10)
GPIO.output(led, GPIO.LOW)
print("Led off.")
GPIO.cleanup()