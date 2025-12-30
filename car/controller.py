from microbit import *
import radio

pin14.set_pull(pin14.PULL_UP)
pin15.set_pull(pin15.PULL_UP)

radio.config(group = 10)
radio.on()

while True:
    btn_a = pin14.read_digital()
    btn_b = pin15.read_digital()
    stck_x = pin1.read_analog()

    if btn_a == 0:
        radio.send("Accelerate")
        display.set_pixel(2,0,9)
    if btn_b == 0:
        radio.send("Brake")
        display.set_pixel(2,4,9)
    if stck_x < 300:
        radio.send("Right")
        display.set_pixel(4,2,9)
    elif stck_x > 723:
        radio.send("Left")
        display.set_pixel(0,2,9)

    sleep(50)

    display.set_pixel(2,0,0)
    display.set_pixel(2,4,0)
    display.set_pixel(4,2,0)
    display.set_pixel(0,2,0)
