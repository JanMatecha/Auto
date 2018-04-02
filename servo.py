import machine
import time


# TEST zapojeni diody
"""
import diody
P = diody.setPin(12)
P.value(1)
time.sleep(3)
P.value(0)
"""


class Servo:
    """
    https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/pwm.html
    7.2. Control a hobby servo

    Hobby servo motors can be controlled using PWM. They require a frequency of 50Hz
    and then a duty between about 40 and 115, with 77 being the centre value.
    If you connect a servo to the power and ground pins, and then the signal
    line to pin 12 (other pins will work just as well), you can control the motor using:
    """

    def __init__(self, pin_number=None, freq=50, duty=77, min_duty=40, max_duty=115, mean_duty=77):
        self.pin_number = pin_number
        self.set_pin(self.pin_number)
        self.init_pwm()
        self.set_freq(freq)
        self.set_duty(duty)
        self.set_min_duty(min_duty)
        self.set_max_duty(max_duty)
        self.set_mean_duty(mean_duty)

    def set_pin(self, pin=None):
        self.pin = machine.Pin(pin)

    def init_pwm(self):
        self.pwm = machine.PWM(self.pin)

    def set_freq(self, freq):
        self.pwm.freq(freq)

    def set_duty(self, duty):
        self.pwm.duty(duty)

    def set_min_duty(self, min_duty):
        self.min_duty=min_duty

    def set_max_duty(self, max_duty):
        self.max_duty=max_duty

    def set_mean_duty(self, mean_duty):
        self.mean_duty=mean_duty

    def deinit_pwm(self):
        self.pwm.deinit()

    def vlevo(self, direction=None):
        if direction is None:
            self.set_duty(self.min_duty)
        else:
            # duty = mean - (mean - min)*direction
            duty=self.mean_duty-(self.mean_duty-self.min_duty)*direction
            print(duty)
            self.set_duty(duty)

    def vpravo(self, direction=None):

        if direction is None:
            self.set_duty(self.max_duty)
        else:
            # duty = mean + (max - mean)*direction
            duty = self.mean_duty+(self.max_duty-self.mean_duty)*direction
            print(duty)
            self.set_duty(duty)

    def rovne(self):
        self.set_duty(self.mean_duty)

    def test(self):
        a=""
        while a!="k":
            a=input()

            if a=="a":
                self.vlevo()
                print("vlevo")
            elif a=="d":
                self.vpravo()
                print("vpravo")
            elif a=="w":
                self.rovne()
                print("rovne")
            elif a=="s":
                self.rovne()
                print("dozadu")
            elif a=="k":
                print("konec")
            else:
                print("a,d,w,k")


if __name__ == "__main__":

    servo = Servo(12, freq=50, duty=40)
    time.sleep(5)
    servo.set_duty(70)
    time.sleep(5)

    servo.deinit_pwm()

"""
print("Zacatek")
p12 = machine.Pin(12)
pwm12 = machine.PWM(p12)


pwm12.freq(50)
pwm12.duty(40)
print("Nastaveno")
print(pwm12)


time.sleep(1)
pwm12.duty(70)
print("Nastaveno")
print(pwm12)
time.sleep(1)


time.sleep(1)
pwm12.duty(115)
print("Nastaveno")
print(pwm12)
time.sleep(1)

pwm12.deinit()

print("Konec")
"""