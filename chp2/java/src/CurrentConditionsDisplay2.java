import java.util.Observable;
import java.util.Observer;

public class CurrentConditionsDisplay2 implements Observer, DisplayElement {
    Observable observable;
    private float temperature;
    private float humidity;

    public CurrentConditionsDisplay2(Observable observable) {
	this.observable = observable;
	observable.addObserver(this);
    }

    public void update(Observable obs, Object arg) {
	if (obs instanceof WeatherData2) {
	    WeatherData2 weatherData2 = (WeatherData2)obs;
	    this.temperature = weatherData2.getTemperature();
	    this.humidity = weatherData2.getHumidity();
	    display();
	}
    }

    public void display() {
	System.out.println("Current conditions: " + temperature + "F degrees and " + humidity + "% humidity");	
    }
}
