from microbit import *
import radio


radio.config(group = 10)
radio.on()

while True:
    msg = str(radio.receive())

    if "A" in msg:
        display.set_pixel(2,0,9)
    elif "B" in msg:
        display.set_pixel(2,4,9)
    if "R" in msg:
        display.set_pixel(4,2,9)
    elif "L" in msg:
        display.set_pixel(0,2,9)

    sleep(10)

    display.set_pixel(2,0,0)
    display.set_pixel(2,4,0)
    display.set_pixel(4,2,0)
    display.set_pixel(0,2,0)
