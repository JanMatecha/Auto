import time
from servo import Servo
servo = Servo(12)

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