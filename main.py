from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

servo = Servo(17)

while True:
    print("SUP")
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)