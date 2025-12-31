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


def set_speed_turn_direction(speed, turn, direction):
    if turn == 0:
        speed_l = speed
        speed_r = speed
    elif turn == 1:
        speed_l = int(speed * 1.2)
        speed_r = int(speed * 0.8)
        if speed_l > 100:
            speed_l = 100
    elif turn == -1:
        speed_l = int(speed * 0.8)
        speed_r = int(speed * 1.2)
        if speed_r > 100:
            speed_r = 100
    set_motors_speed(speed_l * direction, speed_r * direction)

speed = 0
turn = 0
direction = 1

while True:
    msg = radio.receive()
    if msg:
        msg = str(msg)

        if "A" in msg:
            speed += 5
            display.set_pixel(2,0,9)
        elif "B" in msg:
            speed -= 10
            display.set_pixel(2,4,9)
        elif "N" in msg:
            speed -= 2
        if "R" in msg:
            turn = 1
            display.set_pixel(4,2,9)
        elif "L" in msg:
            turn = -1
            display.set_pixel(0,2,9)
        elif "S" in msg:
            turn = 0
        if "D" in msg:
            direction = direction * (-1)
        
        if direction == 1 and speed > 100:
            speed = 100
        if direction == -1 and speed > 30:
            speed = 30
        if speed < 0:
            speed = 0
        set_speed_turn_direction(speed, turn, direction)

        sleep(50)
        display.clear()        

    sleep(5)
