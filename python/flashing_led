
from microbit import *

time_interval = 500.0

while True:
    pin0.write_digital(1)
    display.set_pixel(2,2,9)
    sleep(time_interval)
    pin0.write_digital(0)
    display.set_pixel(2,2,0)
    sleep(time_interval)
    if button_a.was_pressed():
        time_interval *=2
    if button_b.was_pressed():
        time_interval /=2
    if time_interval > 2000:
        time_interval = 2000
    elif time_interval < 125/2:
        time_interval = 125/2
