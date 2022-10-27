import gc
import board
gc.collect()
import analogio
gc.collect()
import busio
gc.collect()
#import rtc
gc.collect()
import digitalio
gc.collect()
from digitalio import DigitalInOut, Direction, Pull
gc.collect()
import time
gc.collect()
import storage
gc.collect()

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D10)

import adafruit_sdcard
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
gc.collect()

import adafruit_pcf8523
i2c = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(i2c)
gc.collect()

l0 = analogio.AnalogIn(board.A0)
l1 = analogio.AnalogIn(board.A1)
l2 = analogio.AnalogIn(board.A2)
l3 = analogio.AnalogIn(board.A3)
l4 = analogio.AnalogIn(board.A4)
l5 = analogio.AnalogIn(board.A5)
l6 = analogio.AnalogIn(board.D0)
l7 = analogio.AnalogIn(board.D1)
l8 = analogio.AnalogIn(board.D3)
l9 = analogio.AnalogIn(board.D4)
gc.collect()
off = DigitalInOut(board.D5)
off.pull = Pull.DOWN

print(gc.mem_free())
while True:
    try:
        with open("/sd/test2.txt", "a") as f:
            t = rtc.datetime
            print(t.tm_mday,t.tm_mon, t.tm_year,t.tm_hour, t.tm_min,\
            l0.value,l1.value,l2.value,l3.value,l4.value,l5.value,l6.value,l7.value,l8.value,l9.value)
            f.write("{}/{}/{} {}:{},{},{},{},{},{},{},{},{},{},{}\r\n".format(t.tm_mon,\
            t.tm_mday, t.tm_year,t.tm_hour, t.tm_min,\
            l0.value,l1.value,l2.value,l3.value,l4.value,l5.value,l6.value,l7.value,l8.value,l9.value))
            print(gc.mem_free())
    except OSError:
        pass
    except RuntimeError:
        pass
    finally:
        time.sleep(2)
        off.pull = Pull.UP
        time.sleep(2)
        off.pull = Pull.DOWN
        time.sleep(2)
        off.pull = Pull.UP
        time.sleep(2)
        off.pull = Pull.DOWN
        time.sleep(2)
        off.pull = Pull.UP