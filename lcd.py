from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("John Kowal is a simp", 1)
    lcd.text("and he sucks ass", 2)
    lcd.text("hope he chokes on", 3)
    lcd.text("cum covered hot dogs", 4)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()