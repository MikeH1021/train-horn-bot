import RPi.GPIO as GPIO
import time

led = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

while True:
GPIO.output(led, GPIO.HIGH)
print("Led turned on.")
time.sleep(1)
GPIO.output(led, GPIO.LOW)
print("Led off.")
time.sleep(1)
GPIO.cleanup()