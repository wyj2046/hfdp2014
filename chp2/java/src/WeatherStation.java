public class WeatherStation {
    public static void main(String[] args) {
	WeatherData2 weatherData2 = new WeatherData2();
	CurrentConditionsDisplay2 currentDisplay2 = new CurrentConditionsDisplay2(weatherData2);
	weatherData2.setMeasurements(80, 65, 30.4f);
	weatherData2.setMeasurements(82, 70, 29.2f);
	weatherData2.setMeasurements(78, 90, 29.2f);
    }
}
