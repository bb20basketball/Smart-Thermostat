import RPi.GPIO as GPIO
import time

class ServoControl(object):

    SERVO_UP_PIN = 03
    SERVO_DOWN_PIN = 05

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        self.servoUp = self.addServo(self.SERVO_UP_PIN)
        self.servoDown = self.addServo(self.SERVO_DOWN_PIN)

    def addServo(self, pin):

        GPIO.setup(pin, GPIO.output)

        servo = GPIO.PWM(pin, 50)
        servo.start(0)

        return servo

    def changeUpDown(upDown):

        if upDown == 'up':
            self.setAngle(90, self.SERVO_UP_PIN, self.servoUp)
            self.setAngle(0, self.SERVO_UP_PIN, self.servoUp)
        elif upDown == 'down':
            self.setAngle(90, self.SERVO_DOWN_PIN, self.servoDown)
            self.setAngle(0, self.SERVO_DOWN_PIN, self.servoDown)

    def setAngle(angle, pin, servo):

        duty = angle/18 + 2
        GPIO.output(pin, True)
        servo.ChangeDutyCycle(duty)
        sleep(.1)
        GPIO.output(pin, False)
        servo.ChangeDutyCycle(0)
