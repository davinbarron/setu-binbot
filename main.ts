radio.onReceivedValue(function (name, value) {
    if (name == "output1") {
        led.toggle(4, 4)
        basic.showNumber(value)
    }
})
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.OBJECTCLASSIFICATION)
huskylens.clearOSD()
radio.setGroup(9)
basic.showIcon(IconNames.Heart)
basic.clearScreen()
basic.forever(function () {
    huskylens.request()
    // Only send data when button A is pressed
    if (input.buttonIsPressed(Button.A)) {
        if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
            radio.sendValue("input1", 1001)
            basic.showString("P")
            basic.pause(1000)
            basic.clearScreen()
        } else if (huskylens.isAppear(2, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
            radio.sendValue("input1", 1002)
            basic.showString("C")
            basic.pause(1000)
            basic.clearScreen()
        } else if (huskylens.isAppear(3, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
            radio.sendValue("input1", 1003)
            basic.showString("CB")
            basic.pause(1000)
            basic.clearScreen()
        } else {
            radio.sendValue("input1", 1004)
            basic.showString("G")
            basic.pause(1000)
            basic.clearScreen()
        }
    }
})
