from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("John Kowal is genuinely", 1)
    lcd.text("a simp", 2)
    lcd.text("and he smells bad ngl", 3)
    lcd.text("why is he alive? who knows", 4)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()