from WeatherData import WeatherData
from CurrentConditionsDisplay import CurrentConditionsDisplay


def main():
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    weatherData.setMeasurements(82, 65, 30.4)
    weatherData.setMeasurements(80, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)


if __name__ == '__main__':
    main()
