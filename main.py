import RPi.GPIO as GPIO
import time

horn = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(horn, GPIO.OUT)


GPIO.output(horn, GPIO.HIGH)
print("Horn turned on.")
time.sleep(0.25)
GPIO.output(horn, GPIO.LOW)
print("Horn off.")
GPIO.cleanup()