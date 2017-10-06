import time

from getTemperature import GetTemperature

class main(object):

    def __init__(self):
        # GPIO stuff

        # current thermostat setpoint (in F degrees)
        self.currentSetpoint = 70

        # temperature API class
        self.getTemp = GetTemperature()
        print (self.getTemp.update())

    def checkTemp(self):
        """
        Checks if thermostat should adjust or not
        """
        pass

    def changeTemp(self, setpoint):
        """
        Uses the servo to set the temperature on the thermostat
        """
        pass

if __name__ == "__main__":
    main()
