from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from datetime import datetime
from pytz import timezone
from time import sleep
import uasyncio

lcd = LCD()


def safe_exit(signum, frame):
    exit(1)
async def lcd_screen():
    while True:
        dt = datetime.now(timezone("US/Eastern"))
        dt = str(dt)
        dt = dt[:-13]
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        
        if "16:20" in dt or "04:20" in dt:
            lcd.text("smoke weed everyday", 1)
            sleep(5)
            lcd.clear()
        else:
            lcd.text(dt, 1)
            sleep(1)
            lcd.clear()

async def main():
    task1 = uasyncio.create_task(lcd_screen())
    await task1

uasyncio.run(main())
