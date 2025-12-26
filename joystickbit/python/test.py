from microbit import *
import sys

pin14.set_pull(pin14.PULL_UP)

while True:
    b = pin14.read_digital()
    if b == 0:
        display.set_pixel(0, 0, 9)
    else:
        display.set_pixel(0, 0, 0)

    x = pin1.read_analog()
    y = pin2.read_analog()

    print("X:", x, " Y:", y, "Btn:", b)
    sleep(500)
