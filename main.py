import time
import threading

from components.getTemperature import GetTemperature
#from components.servoControl import ServoControl

class main(object):

    def __init__(self):
        # GPIO stuff

        # current thermostat setpoint (in F degrees)
        self.currentSetpoint = 70

        self.comfortableTemp = 73

        self.schedule = {"Sunday": (12,15), "Monday": (8,17), "Tuesday": (8,17),
         "Wednesday":(8, 17), "Thursday":(8,17), "Friday":(8,17), "Saturday":(11, 22)}

        # temperature API class
        self.getTemp = GetTemperature()
        #self.servoControl = ServoControl()
        print (self.getTemp.update())
        self.checkTemp()

    def checkTemp(self):
        """
        Checks if thermostat should adjust or not
        """
        currentTemp = self.getTemp.update()
        currentHour =  int(time.strftime("%H"))
        startHour = self.schedule[time.strftime("%A")][0]
        endHour = self.schedule[time.strftime("%A")][1]

        if currentHour > startHour and currentHour < endHour:
            print 'uyp'
        elif currentHour == endHour:
            print 'yo'
            self.changeTemp(self.comfortableTemp)
        elif currentHour == startHour:
            print 'y'
            self.changeAlgo(currentTemp)

        #threading.Timer(60.0, self.checkTemp).start()

    def changeAlgo(self, currentTemp):
        setTemp = currentTemp

        if currentTemp < 69:
            setTemp = 69
        elif currentTemp > 78:
            setTemp = 78

        self.changeTemp(setTemp)

    def changeTemp(self, setpoint):
        """
        Uses the servo to set the temperature on the thermostat
        """
        if setpoint != self.currentSetpoint:
            self.currentSetpoint = setpoint
            print "doing servo stuff"

if __name__ == "__main__":
    main()
