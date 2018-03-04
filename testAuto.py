from motor import Motor
import time
from servo import Servo


servo = Servo(12)
motor=Motor()

velocity=50
duration=1
sleepTime=2
motor.forward(velocity=velocity, duration=duration)
servo.set_duty(80)
motor.forward(velocity=velocity, duration=duration)
time.sleep(sleepTime)
servo.set_duty(70)
motor.forward(velocity=velocity, duration=duration)
time.sleep(sleepTime)
servo.set_duty(90)
motor.forward(velocity=velocity, duration=duration)
time.sleep(sleepTime)
servo.set_duty(77)

servo.deinit_pwm()
