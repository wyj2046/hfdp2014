public class CurrentConditionsDisplay implements Observer, DisplayElement {
    private float tempterature;
    private float humidity;
    private Subject weatherData;

    public CurrentConditionsDisplay(Subject weatherData) {
	this.weatherData = weatherData;
	weatherData.registerObserver(this);
    }

    public void update(float tempterature, float humidity, float pressure) {
	this.tempterature = tempterature;
	this.humidity = humidity;
	display();
    }

    public void display() {
	System.out.println("Current conditions: " + tempterature + "F degrees and " + humidity + "% humidity");
    }
}
