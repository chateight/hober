radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        basic.showArrow(ArrowNames.North)
        stay()
    } else {
        if (receivedNumber == 1) {
            basic.showArrow(ArrowNames.South)
            stop()
        } else {
            if (receivedNumber == 2) {
                basic.showArrow(ArrowNames.NorthWest)
                rot_l()
            } else {
                if (receivedNumber == 3) {
                    basic.showArrow(ArrowNames.NorthEast)
                    rot_r()
                } else {
                    if (receivedNumber == 4) {
                        basic.showArrow(ArrowNames.West)
                        move_l()
                    } else {
                        basic.showArrow(ArrowNames.East)
                        move_r()
                    }
                }
            }
        }
    }
})
function rot_r () {
    pow1 = 1000
    pow2 = 800
    pow3 = 1000
    pow4 = 800
    float()
}
function move_r () {
    pow1 = 1000
    pow2 = 1000
    pow3 = 900
    pow4 = 900
    float()
}
function float () {
    pins.analogSetPeriod(AnalogPin.P0, cycle)
    pins.analogSetPeriod(AnalogPin.P1, cycle)
    pins.analogSetPeriod(AnalogPin.P2, cycle)
    pins.analogSetPeriod(AnalogPin.P8, cycle)
    pins.analogWritePin(AnalogPin.P0, pow1)
    pins.analogWritePin(AnalogPin.P1, pow2)
    pins.analogWritePin(AnalogPin.P2, pow3)
    pins.analogWritePin(AnalogPin.P8, pow4)
}
function move_l () {
    pow1 = 900
    pow2 = 900
    pow3 = 1000
    pow4 = 1000
    float()
}
function stop () {
    pow1 = 0
    pow2 = 0
    pow3 = 0
    pow4 = 0
    float()
}
function rot_l () {
    pow1 = 800
    pow2 = 1000
    pow3 = 800
    pow4 = 1000
    float()
}
function stay () {
    pow1 = 900
    pow2 = 900
    pow3 = 900
    pow4 = 900
    float()
}
let pow4 = 0
let pow3 = 0
let pow2 = 0
let pow1 = 0
let cycle = 0
radio.setGroup(1)
cycle = 20000
