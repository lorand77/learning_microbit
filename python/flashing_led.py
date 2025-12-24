from microbit import *
import math

delay = 500.0

def update_delay():
    global delay
    if button_a.was_pressed():
        delay *= 2
        if delay > 4000:
            delay = 4000
        bar_delay()
    if button_b.was_pressed():
        delay /= 2
        if delay < 125/16:
            delay = 125/16
        bar_delay()

def bar_delay():
    level = int(math.log(delay/(125/16))/math.log(2))
    for i in range(10):
        display.set_pixel(i%5, i//5, 0)
    for i in range(level+1):
        if i < 5:
            display.set_pixel(i, 0, 9)
        else:
            display.set_pixel(i-5, 1, 9)
    print(delay)

bar_delay()
while True:
    pin0.write_digital(1)
    display.set_pixel(2,3,0)
    display.set_pixel(2,4,9)
    sleep(delay)
    update_delay()

    pin0.write_digital(0)
    display.set_pixel(2,3,9)
    display.set_pixel(2,4,0)
    sleep(delay)
    update_delay()
