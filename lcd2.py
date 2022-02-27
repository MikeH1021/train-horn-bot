from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import sleep
lcd = LCD()


def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

while True:
    lcd.text("H", 1)
    sleep(1)
    lcd.clear()
    sleep(1)
    lcd.text("K", 1)
    sleep(1)
    lcd.clear()