import d1motor, time
from machine import I2C, Pin





class Motor(object):

    def __init__(self):
        self.i2c = I2C(scl=Pin(5), sda=Pin(4))
        self.m1 = d1motor.Motor(0, self.i2c)
        self.m2 = d1motor.Motor(1, self.i2c)

    def go(self, velocity=None, duration=None, direction=None):
        if duration is None:
            duration = 0.5
        if velocity is None:
            velocity = 500
        if direction is None:
            direction = 1

        self.m1.speed(velocity*direction)
        self.m2.speed(velocity*direction)
        time.sleep(duration)
        self.m1.speed(0)
        self.m2.speed(0)

    def forward(self,velocity=None, duration=None):
        self.go(velocity=velocity, duration=duration, direction=1)

    def backward(self,velocity=None, duration=None):
        self.go(velocity=velocity, duration=duration, direction=-1)