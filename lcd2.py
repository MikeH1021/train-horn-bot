from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import sleep
lcd = LCD()


def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    lcd.text("Hello World", 1)
    sleep(1)
    lcd.clear()
    lcd.text("Youre a bitch", 1)

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()