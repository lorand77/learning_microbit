from microbit import *

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


if __name__ == '__main__':
    set_motors_speed(30, 50)
    set_car_light("left", 30, 30, 90)
    sleep(3000)
    set_motors_speed(0, 0)
