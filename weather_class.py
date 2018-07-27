from weather import Weather, Unit
from datetime import datetime
from googletrans import Translator

# TODO klassifizierung, wetter gut schlecht mittelmäßig

def weather(loc="Berlin"):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(loc)
    forecasts = location.forecast
    print(forecasts)
    for forecast in forecasts:
        print(forecast.date)
        if forecast.date == datetime.now().strftime("%d %b %Y"):
            text = translate(forecast.text)
            text = "Das Wetter ist heute " + text + ". Es kann " + forecast.low + " bis " + forecast.high + " Grad warm werden."
            return text

def translate(text):
    translator = Translator()
    translation = translator.translate(text, dest="de")
    return translation.text