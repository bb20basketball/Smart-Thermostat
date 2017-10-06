import urllib
import json

class GetTemperature(object):

    def __init__(self):

        pass

    def update(self):
        self.getData = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?q=minneapolis,us&APPID=e43c3669282ae317bc20c475813df4b7')
        self.dataToJSON = json.load(self.getData)
        return self.convertToFahreheit(self.dataToJSON['main']['temp'])

    def convertToFahreheit(self, kelvin):
        return ((kelvin*9/5) - 459.67)
