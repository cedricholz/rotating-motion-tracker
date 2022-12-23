import RPi.GPIO as GPIO
import time

from gpiozero import Servo

servo = Servo(13)
print("MAX")
servo.max()

time.sleep(5)
print("MIN")
servo.min()

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(12, GPIO.OUT)
# p = GPIO.PWM(12, 50)
# p.start(2.1)
# time.sleep(1)
#
# for angle in range(2, 180):
#     duty = float(angle) / 18 + 2
#     print(duty)
#
#     p.ChangeDutyCycle(duty)
#     time.sleep(0.015)
#
# for angle in range(180, 2, -1):
#     duty = float(angle) / 18 + 2
#     print(duty)
#
#     p.ChangeDutyCycle(duty)
#     time.sleep(0.015)
#
# time.sleep(3)
#
# GPIO.cleanup()

# import time
#
# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BOARD)
#
# servoPin = 12
#
# GPIO.setup(servoPin, GPIO.OUT)  # Set servoPin to OUTPUT mode
# GPIO.output(servoPin, GPIO.LOW)  # Make servoPin output LOW level
#
# p = GPIO.PWM(servoPin, 50)
# # p = GPIO.PWM(servoPin, 50)  # set Frequece to 50Hz
# p.start(0)  # Set initial Duty Cycle to 0
#
#
# def setAngle(angle):
#     print("SET LOCAL")
#     duty = float(angle) / 10 + 2.5
#     p.ChangeDutyCycle(duty)
#     time.sleep(0.015)


# i = 0
# while True:
#     if i % 2 == 0:
#         setAngle(0)
#     else:
#         setAngle(45)
#     time.sleep(5)
#     i += 1
#
#
# GPIO.cleanup()
# c.close()
#
# GPIO.setwarnings(False)
#
# # pir = MotionSensor(13, threshold=.8)
# servo = Servo(12)
#
#
# OFFSE_DUTY = 0.5  # define pulse offset of servo
# SERVO_MIN_DUTY = 2.5 + OFFSE_DUTY  # define pulse duty cycle for minimum angle of servo
# SERVO_MAX_DUTY = 12.5 + OFFSE_DUTY  # define pulse duty cycle for maximum angle of servo
# servoPin = 12
#
#
# def map(value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
#     return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow
#
#
# def setup():
#     global p
#     # GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
#     GPIO.setup(servoPin, GPIO.OUT)  # Set servoPin to OUTPUT mode
#     GPIO.output(servoPin, GPIO.LOW)  # Make servoPin output LOW level
#
#     p = GPIO.PWM(servoPin, 50)  # set Frequece to 50Hz
#     p.start(0)  # Set initial Duty Cycle to 0
#
#
# def servoWrite(angle):  # make the servo rotate to specific angle, 0-180
#     if (angle < 0):
#         angle = 0
#     elif (angle > 180):
#         angle = 180
#     p.ChangeDutyCycle(map(angle, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))  # map the angle to duty cycle and output it
#
#
# def loop():
#     while True:
#         for dc in range(0, 181, 1):  # make servo rotate from 0 to 180 deg
#             servoWrite(dc)  # Write dc value to servo
#             time.sleep(0.001)
#         time.sleep(0.5)
#         for dc in range(180, -1, -1):  # make servo rotate from 180 to 0 deg
#             servoWrite(dc)
#             time.sleep(0.001)
#         time.sleep(0.5)
#
#
# def destroy():
#     p.stop()
#     GPIO.cleanup()
#
#
# if __name__ == '__main__':  # Program entrance
#     print('Program is starting...')
#     setup()
#     try:
#         loop()
#     except KeyboardInterrupt:  # Press ctrl-c to end the program.
#         destroy()
#
#
# print("START")
#
#
# pir.wait_for_motion()
# i = 0
# while True:
#     print("SUP")
#     pir.wait_for_motion()
#     # if i % 2 == 0:
#     #     print("MOVING MAX")
#     #     servo.value = .5
#     # else:
#     #     print("MOVING MIN")
#     #     servo.value = 0
#     pir.wait_for_no_motion()
#     i += 1
#     # if pir.motion_detected:
#     #     print("oh yea")
#
#     # time.sleep(.25)


# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BOARD)  # Set GPIO to pin numbering
# pir = 13  # Assign pin 8 to PIR
# # led = 10  # Assign pin 10 to LED
# GPIO.setup(pir, GPIO.IN)  # Setup GPIO pin PIR as input
# # GPIO.setup(led, GPIO.OUT)  # Setup GPIO pin for LED as output
# print("Sensor initializing . . .")
# time.sleep(2)  # Give sensor time to startup
# print("Active")
# print("Press Ctrl+c to end program")
#
# try:
#     while True:
#         print("WUP")
#         if GPIO.input(pir) == True:  # If PIR pin goes high, motion is detected
#             print("Motion Detected!")
#             # GPIO.output(led, True)  # Turn on LED
#             time.sleep(4)  # Keep LED on for 4 seconds
#             # GPIO.output(led, False)  # Turn off LED
#             time.sleep(0.1)
#         time.speel(0.1)
#
# except KeyboardInterrupt:  # Ctrl+c
#     pass  # Do nothing, continue to finally
#
# finally:
#     # GPIO.output(led, False)  # Turn off LED in case left on
#     GPIO.cleanup()  # reset all GPIO
#     print("Program ended")

# servo = Servo(12)
#
# while True:
#     print("SUP")
#     servo.min()
#     sleep(1)
#     servo.mid()
#     sleep(1)
#     servo.max()
#     sleep(1)
