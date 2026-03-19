def on_received_value(name, value):
    if name == "output1":
        led.toggle(4, 4)
        basic.show_number(value)
radio.on_received_value(on_received_value)

huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.OBJECTCLASSIFICATION)
huskylens.clear_osd()
radio.set_group(9)
basic.show_icon(IconNames.HEART)
basic.clear_screen()

def on_forever():
    huskylens.request()
    # Only send data when button A is pressed
    if input.button_is_pressed(Button.A):
        if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            radio.send_value("input1", 1001)
            basic.show_string("P")
            basic.pause(1000)
            basic.clear_screen()
        elif huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            radio.send_value("input1", 1002)
            basic.show_string("C")
            basic.pause(1000)
            basic.clear_screen()
        elif huskylens.is_appear(3, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            radio.send_value("input1", 1003)
            basic.show_string("CB")
            basic.pause(1000)
            basic.clear_screen()
        else:
            radio.send_value("input1", 1004)
            basic.show_string("G")
            basic.pause(1000)
            basic.clear_screen()
basic.forever(on_forever)
