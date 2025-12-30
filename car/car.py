from microbit import *
import radio

radio.config(group = 10)
radio.on()

CUTEBOT_ADDR = 0x10
i2c.init()

def set_motors_speed(left_wheel_speed, right_wheel_speed):
    left_direction = 0x02 if left_wheel_speed > 0 else 0x01
    right_direction = 0x02 if right_wheel_speed > 0 else 0x01
    left_wheel_speed = left_wheel_speed if left_wheel_speed > 0 else left_wheel_speed * -1
    right_wheel_speed = right_wheel_speed if right_wheel_speed > 0 else right_wheel_speed * -1
    i2c.write(CUTEBOT_ADDR, bytearray([0x01, left_direction, left_wheel_speed, 0]))
    i2c.write(CUTEBOT_ADDR, bytearray([0x02, right_direction, right_wheel_speed, 0]))

def set_car_light(light, R, G, B):
    light_bytecode = 0x04 if light == "left" else 0x08
    i2c.write(CUTEBOT_ADDR, bytearray([light_bytecode, R, G, B]))

speed_l = 0
speed_r = 0
direction = 0

while True:
    msg = radio.receive()
    if msg is None:
        msg = ""
    else:
        msg = str(msg)

    if "A" in msg:
        speed_l += 5
        speed_r += 5
        if speed_l > 100:
            speed_l = 100
        if speed_r > 100:
            speed_r = 100
        set_motors_speed(speed_l, speed_r)
        display.set_pixel(2,0,9)
    elif "B" in msg:
        speed_l -= 10
        speed_r -= 10
        if speed_l < 0:
            speed_l = 0
        if speed_r < 0:
            speed_r = 0
        set_motors_speed(speed_l, speed_r)
        display.set_pixel(2,4,9)
    elif "N" in msg:
        speed_l -= 2
        speed_r -= 2
        if speed_l < 0:
            speed_l = 0
        if speed_r < 0:
            speed_r = 0
        set_motors_speed(speed_l, speed_r)
    if "R" in msg:
        direction = 1
        speed = (speed_l + speed_r) // 2
        speed_l = int(speed * (1 + direction*0.2))
        speed_r = int(speed * (1 - direction*0.2))
        set_motors_speed(speed_l, speed_r)
        if speed_l > 100:
            speed_l = 100
        if speed_r < 0:
            speed_r = 0
        display.set_pixel(4,2,9)
    elif "L" in msg:
        direction = -1
        speed = (speed_l + speed_r) // 2
        speed_l = int(speed * (1 + direction*0.2))
        speed_r = int(speed * (1 - direction*0.2))
        set_motors_speed(speed_l, speed_r)
        if speed_r > 100:
            speed_r = 100
        if speed_l < 0:
            speed_l = 0
        display.set_pixel(0,2,9)
    elif "S" in msg:
        direction = 0
        speed = (speed_l + speed_r) // 2
        speed_l = speed
        speed_r = speed
        set_motors_speed(speed_l, speed_r)

    sleep(10)

    display.set_pixel(2,0,0)
    display.set_pixel(2,4,0)
    display.set_pixel(4,2,0)
    display.set_pixel(0,2,0)
