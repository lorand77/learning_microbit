from microbit import *
import radio


radio.config(group = 10)
radio.on()

while True:
    msg = radio.receive()

    if msg == "Accelerate":
        display.set_pixel(2,0,9)
    if msg == "Brake":
        display.set_pixel(2,4,9)
    if msg == "Right":
        display.set_pixel(4,2,9)
    elif msg == "Left":
        display.set_pixel(0,2,9)

    sleep(5)

    display.set_pixel(2,0,0)
    display.set_pixel(2,4,0)
    display.set_pixel(4,2,0)
    display.set_pixel(0,2,0)
