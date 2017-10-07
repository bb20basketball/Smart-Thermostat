import time

from getTemperature import GetTemperature
from servoControl import ServoControl

class main(object):

    def __init__(self):
        # GPIO stuff

        # current thermostat setpoint (in F degrees)
        self.currentSetpoint = 70

        # temperature API class
        self.getTemp = GetTemperature()
        self.servoControl = ServoControl()
        print (self.getTemp.update())

    def checkTemp(self):
        """
        Checks if thermostat should adjust or not
        """
        currentTemp = self.getTemp.update()

    def changeTemp(self, setpoint):
        """
        Uses the servo to set the temperature on the thermostat
        """
        pass

if __name__ == "__main__":
    main()
