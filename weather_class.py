from weather import Weather, Unit
from datetime import datetime

# TODO translation

def weather():
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location("freigericht")
    forecasts = location.forecast
    print(forecasts)
    text = ""
    for forecast in forecasts:
        print(forecast.date)
        if forecast.date == datetime.now().strftime("%d %b %Y"):
            text = "Das Wetter ist heute " + forecast.text + ". Es kann " + forecast.low + " bis zu " + forecast.high + " Grad warm werden."
            return text
