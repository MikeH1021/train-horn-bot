from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from datetime import datetime
from pytz import timezone

lcd = LCD()


def safe_exit(signum, frame):
    exit(1)
while True:
    dt = datetime.now(timezone("US/Eastern"))
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text(str(dt), 1)
    lcd.clear()