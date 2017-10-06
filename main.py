import json
import urllib

class getTemperature(object):

    def __init__(self):

        self.update()

    def update(self):

        self.getData = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?q=minneapolis,us&APPID=e43c3669282ae317bc20c475813df4b7')
        self.dataToJSON = json.load(self.getData)
        print self.dataToJSON['main']['temp']

class main(object):

    def __init__(self):
        # GPIO stuff
        pass

    def checkTemp(self):

        pass

if __name__ == "__main__":
    # just testing for now
    getTemperature()
