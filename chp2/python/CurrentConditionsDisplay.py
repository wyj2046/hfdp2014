from Observer import Observer
from DisplayElement import DisplayElement


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        super(CurrentConditionsDisplay, self).__init__()
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print "Current conditions: %sF degrees and %s%% humidity" % (self.temperature, self.humidity)
