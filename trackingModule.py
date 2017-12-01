import RPi.GPIO as GPIO


class trackingModule:
    # ------------------ #
    leftmostled_pin = 16
    leftlessled_pin = 18
    centerled_pin = 22
    rightlessled_pin = 40
    rightmostled_pin = 32
    # ------------------ #
    lmost_v = 0
    lless_v = 0
    center_v = 0
    rless_v = 0
    rmost_v = 0
    # ------------------ #
    started = False

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    def pinSetup(self):
        GPIO.setup(self.leftmostled_pin, GPIO.IN)
        GPIO.setup(self.leftlessled_pin, GPIO.IN)
        GPIO.setup(self.centerled_pin, GPIO.IN)
        GPIO.setup(self.rightlessled_pin, GPIO.IN)
        GPIO.setup(self.rightmostled_pin, GPIO.IN)

    def setup(self):
        self.pinSetup()
        self.loop()

    def lmost(self):
        return self.lmost_v

    def lless(self):
        return self.lless_v

    def center(self):
        return self.center_v

    def rless(self):
        return self.rless_v

    def rmost(self):
        return self.rmost_v

    def isForward(self):
        print("isForward")
        return self.center_v == 0

    def isSemiLeft(self):
        print("isSemiLeft")
        return (self.lless_v == 1 and self.center_v == 0 and self.rless_v == 0)

    def isSemiRight(self):
        print("isSemiRight")
        return (self.lless_v == 0 and self.center_v == 0 and self.rless_v == 1)

    def isStop(self):
        print("isStop")
        return (self.lmost == 1 and self.lless_v == 1 and self.center_v == 1 and self.rless_v == 1  and self.rmost_v == 1)