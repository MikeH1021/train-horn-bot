from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("John Kowal is a simp", 1)
    lcd.text("whoever gave birth to him", 2)
    lcd.text("needs to reconsider life", 3)
    lcd.text("hope he chokes on saliva", 4)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()