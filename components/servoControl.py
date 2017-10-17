import RPi.GPIO as GPIO
from time import sleep

class ServoControl(object):

    SERVO_UP_PIN = 3
    SERVO_DOWN_PIN = 5

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        self.servoUp = self.addServo(self.SERVO_UP_PIN)
        self.servoDown = self.addServo(self.SERVO_DOWN_PIN)

    def addServo(self, pin):
	print pin
	print type(pin)
        GPIO.setup(pin, GPIO.OUT)

        servo = GPIO.PWM(pin, 50)
        servo.start(0)

        return servo

    def changeUpDown(self, upDown):

        if upDown == 'up':
            self.setAngle(90, self.SERVO_UP_PIN, self.servoUp)
            self.setAngle(0, self.SERVO_UP_PIN, self.servoUp)
        elif upDown == 'down':
            self.setAngle(90, self.SERVO_DOWN_PIN, self.servoDown)
            self.setAngle(0, self.SERVO_DOWN_PIN, self.servoDown)

    def setAngle(self, angle, pin, servo):

        duty = angle/18 + 2
        GPIO.output(pin, True)
        servo.ChangeDutyCycle(duty)
        sleep(2)
        GPIO.output(pin, False)
        servo.ChangeDutyCycle(0)
