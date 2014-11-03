import java.util.*;


public class WeatherData implements Subject {
    private float tempterature;
    private float humidity;
    private float pressure;
    private ArrayList observers;

    public WeatherData() {
	observers = new ArrayList();
    }

    public void registerObserver(Observer o) {
	observers.add(o);
    }

    public void removeObserver(Observer o) {
	int i = observers.indexOf(o);
	if (i >= 0) {
	    observers.remove(i);
	}
    }

    public void notifyObserver() {
	for (int i = 0; i < observers.size(); i++) {
	    Observer observer = (Observer)observers.get(i);
	    observer.update(tempterature, humidity, pressure);
	}
    }

    public void measurementsChanged() {
	notifyObserver();
    }

    public void setMeasurements(float tempterature, float humidity, float pressure) {
	this.tempterature = tempterature;
	this.humidity = humidity;
	this.pressure = pressure;
	measurementsChanged();
    }
}
