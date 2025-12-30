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

    msg = ""
    if btn_a == 0:
        msg = "A"
        display.set_pixel(2,0,9)
    elif btn_b == 0:
        msg = msg + "B"
        display.set_pixel(2,4,9)
    if stck_x < 300:
        msg = msg + "R"
        display.set_pixel(4,2,9)
    elif stck_x > 723:
        msg = msg + "L"
        display.set_pixel(0,2,9)
    radio.send(msg)

    sleep(100)

    display.set_pixel(2,0,0)
    display.set_pixel(2,4,0)
    display.set_pixel(4,2,0)
    display.set_pixel(0,2,0)
