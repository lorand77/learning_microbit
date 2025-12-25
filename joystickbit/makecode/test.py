def my_function():
    basic.show_leds("""
        # # # . .
        # . . # .
        # # # . .
        # . . # .
        # # # . .
        """)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def my_function2():
    basic.show_leds("""
        . # # . .
        # . . # .
        # # # # .
        # . . # .
        # . . # .
        """)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

joystickbit.init_joystick_bit()

def on_forever():
    serial.write_line("" + str(joystickbit.get_rocker_value(joystickbit.rockerType.X)))
    serial.write_line("" + str(joystickbit.get_rocker_value(joystickbit.rockerType.Y)))
    basic.pause(500)
basic.forever(on_forever)
