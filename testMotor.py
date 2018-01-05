import d1motor
from machine import I2C, Pin
#https://bitbucket.org/thesheep/micropython-d1motor/issues/1/example-code-is-outdated
#porad nefunguje
#i2c = I2C(scl=Pin(5), sda=Pin(4))
#i2c = I2C(-1, Pin(5), Pin(4), freq=100000)
i2c = I2C(-1, Pin(5), Pin(4), freq=100000)
m1 = d1motor.Motor(0, i2c)
#m2 = d1motor.Motor(1, i2c)
m1.speed(5000)
#m2.speed(5000)