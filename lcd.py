from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from datetime import datetime
from pytz import timezone

lcd = LCD()

dt = datetime.now(timezone("US/Eastern"))

def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text(str(dt), 1)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()