def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_arrow(ArrowNames.NORTH)
        stay()
    else:
        if receivedNumber == 1:
            basic.show_arrow(ArrowNames.SOUTH)
            stop()
        else:
            if receivedNumber == 2:
                basic.show_arrow(ArrowNames.NORTH_WEST)
                rot_l()
            else:
                if receivedNumber == 3:
                    basic.show_arrow(ArrowNames.NORTH_EAST)
                    rot_r()
                else:
                    if receivedNumber == 4:
                        basic.show_arrow(ArrowNames.WEST)
                        move_l()
                    else:
                        basic.show_arrow(ArrowNames.EAST)
                        move_r()
radio.on_received_number(on_received_number)

def rot_r():
    global pow1, pow2, pow3, pow4
    pow1 = 1000
    pow2 = 800
    pow3 = 1000
    pow4 = 800
    float2()
def move_r():
    global pow1, pow2, pow3, pow4
    pow1 = 1000
    pow2 = 1000
    pow3 = 900
    pow4 = 900
    float2()
def float2():
    pins.analog_set_period(AnalogPin.P0, cycle)
    pins.analog_set_period(AnalogPin.P1, cycle)
    pins.analog_set_period(AnalogPin.P2, cycle)
    pins.analog_set_period(AnalogPin.P8, cycle)
    pins.analog_write_pin(AnalogPin.P0, pow1)
    pins.analog_write_pin(AnalogPin.P1, pow2)
    pins.analog_write_pin(AnalogPin.P2, pow3)
    pins.analog_write_pin(AnalogPin.P8, pow4)
def move_l():
    global pow1, pow2, pow3, pow4
    pow1 = 900
    pow2 = 900
    pow3 = 1000
    pow4 = 1000
    float2()
def stop():
    global pow1, pow2, pow3, pow4
    pow1 = 0
    pow2 = 0
    pow3 = 0
    pow4 = 0
    float2()
def rot_l():
    global pow1, pow2, pow3, pow4
    pow1 = 800
    pow2 = 1000
    pow3 = 800
    pow4 = 1000
    float2()
def stay():
    global pow1, pow2, pow3, pow4
    pow1 = 900
    pow2 = 900
    pow3 = 900
    pow4 = 900
    float2()
pow4 = 0
pow3 = 0
pow2 = 0
pow1 = 0
cycle = 0
radio.set_group(1)
cycle = 20000