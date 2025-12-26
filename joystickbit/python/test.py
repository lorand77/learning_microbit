from microbit import *

pin14.set_pull(pin14.PULL_UP)

while True:
    x = pin14.read_digital()
    if x == 0:
        display.set_pixel(0, 0, 9)
    else:
        display.set_pixel(0, 0, 0)
    print(x)
    sleep(300)
