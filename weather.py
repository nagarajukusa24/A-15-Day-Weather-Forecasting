import requests


class Weather():

    def __init__(self, config):
        self.location = None
        self.config = config

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def download_weather_data(self):
        params = {
            'q': self.location,
            'appid': self.config['API_KEY'],
            'units': 'metric'
        }
        try:
            response = requests.get(self.config['API_URL'], params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise WeatherException("Weather for {} not found".format(self.location))

    def get_forecast_data(self):
        weather = self.download_weather_data()
        w = weather['list']
        current = w[0]['weather'][0]['description'], w[0]['main']['temp'],w[0]['main']['humidity'],w[0]['wind']['speed']
        tomorrow = w[1]['weather'][0]['description'], w[1]['main']['temp']
        dayafter = w[2]['weather'][0]['description'], w[2]['main']['temp']



        currentt = w[4]['weather'][0]['description'], w[4]['main']['temp']
        tomorroww = w[5]['weather'][0]['description'], w[5]['main']['temp']
        dayafterr = w[6]['weather'][0]['description'], w[6]['main']['temp']
        dayafterr_ = w[7]['weather'][0]['description'], w[7]['main']['temp']
        dayafterr__ = w[8]['weather'][0]['description'], w[8]['main']['temp']

        day = w[9]['weather'][0]['description'], w[9]['main']['temp']
        day_ = w[10]['weather'][0]['description'], w[10]['main']['temp']
        day__ = w[11]['weather'][0]['description'], w[11]['main']['temp']

        today = w[12]['weather'][0]['description'], w[12]['main']['temp']
        today_ = w[13]['weather'][0]['description'], w[13]['main']['temp']
        today__ = w[14]['weather'][0]['description'], w[14]['main']['temp']
        today___ = w[15]['weather'][0]['description'], w[15]['main']['temp']



        return weather['city']['name'], current, tomorrow, dayafter, currentt, tomorroww, dayafterr, dayafterr_, dayafterr__, day, day_,day__,today, today_,today__,today___#, currentt_, tomorroww_, dayafterr_


class WeatherException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "Weather not found!"
