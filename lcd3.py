from signal import signal, SIGTERM, SIGHUP, pause
import time
from rpi_lcd import LCD
from datetime import datetime
from pytz import timezone
from time import sleep

lcd = LCD()


def safe_exit(signum, frame):
    exit(1)

while True:
        lcd.text("smoke weed everyday", 1)

        sleep(1)
        lcd.clear()