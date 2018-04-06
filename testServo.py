import time
from servo import Servo
servo = Servo(pin_number=12, freq=50, duty=70, min_duty=60, max_duty=80, mean_duty=70)
servo.set_duty(80)
time.sleep(5)
servo.set_duty(80)
time.sleep(5)
servo.set_duty(70)
time.sleep(5)
servo.set_duty(90)
time.sleep(5)
servo.set_duty(77)

servo.deinit_pwm()

"""

import diody
print("Zacatek dioda")
P = diody.setPins([12])
diody.blik(2,P)
print("Zacatek servo")

servo = Servo(12)

time.sleep(5)
servo.set_duty(70)
time.sleep(5)
servo.set_duty(100)
time.sleep(5)
servo.deinit_pwm()
print("Konec servo")
diody.blik(2,P)
print("Konec dioda")
"""