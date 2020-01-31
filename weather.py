# import requests


# class Weather():

#     def __init__(self, config):
#         self.location = None
#         self.config = config

#     def set_location(self, location):
#         self.location = location

#     def get_location(self):
#         return self.location

#     def download_weather_data(self):
#         params = {
#             'q': self.location,
#             'appid': self.config['API_KEY'],
#             'units': 'metric'
#         }
#         try:
#             response = requests.get(self.config['API_URL'], params=params)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.HTTPError:
#             raise WeatherException("Weather for {} not found".format(self.location))

#     def get_forecast_data(self):
#         weather = self.download_weather_data()
#         w = weather['list']
        
#         current = w[0]['weather'][0]['description'], w[0]['main']['temp'], w[0]['main']['temp_max'], w[0]['main']['humidity'], w[0]['wind']['speed']
#         tomorrow = w[1]['weather'][0]['description'], w[1]['main']['temp'], w[1]['main']['temp_max'], w[1]['main']['humidity'], w[1]['wind']['speed']
#         day3 = w[2]['weather'][0]['description'], w[2]['main']['temp'], w[2]['main']['temp_max'], w[2]['main']['humidity'], w[2]['wind']['speed']



#         day4 = w[3]['weather'][0]['description'], w[3]['main']['temp'], w[3]['main']['temp_max'], w[3]['main']['humidity'], w[3]['wind']['speed']
#         #day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['temp_max'], w[4]['main']['humidity'], w[4]['wind']['speed']
#         day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['temp_max'], w[4]['main']['humidity'], w[4]['wind']['speed']

#         day6 = w[5]['weather'][0]['description'], w[5]['main']['temp'], w[5]['main']['temp_max'], w[5]['main']['humidity'], w[5]['wind']['speed']
#         day7 = w[6]['weather'][0]['description'], w[6]['main']['temp'], w[6]['main']['temp_max'], w[6]['main']['humidity'], w[6]['wind']['speed']
#         day8 = w[7]['weather'][0]['description'], w[7]['main']['temp'], w[7]['main']['temp_max'], w[7]['main']['humidity'], w[7]['wind']['speed']

#         day9 = w[8]['weather'][0]['description'], w[8]['main']['temp'], w[8]['main']['temp_max'], w[8]['main']['humidity'], w[8]['wind']['speed']
#         day10 = w[9]['weather'][0]['description'], w[9]['main']['temp'], w[9]['main']['temp_max'], w[9]['main']['humidity'], w[9]['wind']['speed']
#         day11 = w[10]['weather'][0]['description'], w[10]['main']['temp'], w[10]['main']['temp_max'], w[10]['main']['humidity'], w[10]['wind']['speed']

#         day12 = w[11]['weather'][0]['description'], w[11]['main']['temp'], w[11]['main']['temp_max'], w[11]['main']['humidity'], w[11]['wind']['speed']
#         day13 = w[12]['weather'][0]['description'], w[12]['main']['temp'], w[12]['main']['temp_max'], w[12]['main']['humidity'], w[12]['wind']['speed']
#         day14 = w[13]['weather'][0]['description'], w[13]['main']['temp'], w[13]['main']['temp_max'], w[13]['main']['humidity'], w[13]['wind']['speed']
#         day15 = w[14]['weather'][0]['description'], w[14]['main']['temp'], w[14]['main']['temp_max'], w[14]['main']['humidity'], w[14]['wind']['speed']

#         current = w[0]['weather'][0]['description'], w[0]['main']['temp'], w[0]['main']['humidity'], w[0]['wind']['speed']
#         tomorrow = w[1]['weather'][0]['description'], w[1]['main']['temp'], w[1]['main']['humidity'], w[1]['wind']['speed']
#         day3 = w[2]['weather'][0]['description'], w[2]['main']['temp'], w[2]['main']['humidity'], w[2]['wind']['speed']



#         day4 = w[3]['weather'][0]['description'], w[3]['main']['temp'], w[3]['main']['humidity'], w[3]['wind']['speed']
#         #day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['temp_max'], w[4]['main']['humidity'], w[4]['wind']['speed']
#         day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['humidity'], w[4]['wind']['speed']

#         day6 = w[5]['weather'][0]['description'], w[5]['main']['temp'], w[5]['main']['humidity'], w[5]['wind']['speed']
#         day7 = w[6]['weather'][0]['description'], w[6]['main']['temp'], w[6]['main']['humidity'], w[6]['wind']['speed']
#         day8 = w[7]['weather'][0]['description'], w[7]['main']['temp'], w[7]['main']['humidity'], w[7]['wind']['speed']

#         day9 = w[8]['weather'][0]['description'], w[8]['main']['temp'], w[8]['main']['humidity'], w[8]['wind']['speed']
#         day10 = w[9]['weather'][0]['description'], w[9]['main']['temp'], w[9]['main']['humidity'], w[9]['wind']['speed']
#         day11 = w[10]['weather'][0]['description'], w[10]['main']['temp'], w[10]['main']['humidity'], w[10]['wind']['speed']

#         day12 = w[11]['weather'][0]['description'], w[11]['main']['temp'], w[11]['main']['humidity'], w[11]['wind']['speed']
#         day13 = w[12]['weather'][0]['description'], w[12]['main']['temp'], w[12]['main']['humidity'], w[12]['wind']['speed']
#         day14 = w[13]['weather'][0]['description'], w[13]['main']['temp'], w[13]['main']['humidity'], w[13]['wind']['speed']
#         day15 = w[14]['weather'][0]['description'], w[14]['main']['temp'], w[14]['main']['humidity'], w[14]['wind']['speed']

#        # return weather['city']['name'], current, tomorrow, dayafter, currentt, tomorroww, dayafterr, dayafterr_, dayafterr__, day, day_,day__,today, today_,today__,today___#, currentt_, tomorroww_, dayafterr_
#         return weather['city']['name'], current, tomorrow, day3, day4, day5, day6, day7, day8, day9, day10,day11,day12, day13,day14,day15

# class WeatherException(Exception):

#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None

#     def __str__(self):
#         if self.message:
#             return self.message
#         else:
#             return "Weather not found!"
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
        '''  
        current = w[0]['weather'][0]['description'], w[0]['main']['temp'], w[0]['main']['temp_max'], w[0]['main']['humidity'], w[0]['wind']['speed']
        tomorrow = w[1]['weather'][0]['description'], w[1]['main']['temp'], w[1]['main']['temp_max'], w[1]['main']['humidity'], w[1]['wind']['speed']
        day3 = w[2]['weather'][0]['description'], w[2]['main']['temp'], w[2]['main']['temp_max'], w[2]['main']['humidity'], w[2]['wind']['speed']



        day4 = w[3]['weather'][0]['description'], w[3]['main']['temp'], w[3]['main']['temp_max'], w[3]['main']['humidity'], w[3]['wind']['speed']
        #day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['temp_max'], w[4]['main']['humidity'], w[4]['wind']['speed']
        day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['temp_max'], w[4]['main']['humidity'], w[4]['wind']['speed']

        day6 = w[5]['weather'][0]['description'], w[5]['main']['temp'], w[5]['main']['temp_max'], w[5]['main']['humidity'], w[5]['wind']['speed']
        day7 = w[6]['weather'][0]['description'], w[6]['main']['temp'], w[6]['main']['temp_max'], w[6]['main']['humidity'], w[6]['wind']['speed']
        day8 = w[7]['weather'][0]['description'], w[7]['main']['temp'], w[7]['main']['temp_max'], w[7]['main']['humidity'], w[7]['wind']['speed']

        day9 = w[8]['weather'][0]['description'], w[8]['main']['temp'], w[8]['main']['temp_max'], w[8]['main']['humidity'], w[8]['wind']['speed']
        day10 = w[9]['weather'][0]['description'], w[9]['main']['temp'], w[9]['main']['temp_max'], w[9]['main']['humidity'], w[9]['wind']['speed']
        day11 = w[10]['weather'][0]['description'], w[10]['main']['temp'], w[10]['main']['temp_max'], w[10]['main']['humidity'], w[10]['wind']['speed']

        day12 = w[11]['weather'][0]['description'], w[11]['main']['temp'], w[11]['main']['temp_max'], w[11]['main']['humidity'], w[11]['wind']['speed']
        day13 = w[12]['weather'][0]['description'], w[12]['main']['temp'], w[12]['main']['temp_max'], w[12]['main']['humidity'], w[12]['wind']['speed']
        day14 = w[13]['weather'][0]['description'], w[13]['main']['temp'], w[13]['main']['temp_max'], w[13]['main']['humidity'], w[13]['wind']['speed']
        day15 = w[14]['weather'][0]['description'], w[14]['main']['temp'], w[14]['main']['temp_max'], w[14]['main']['humidity'], w[14]['wind']['speed']

        '''
        current = w[0]['weather'][0]['description'], w[0]['main']['temp'], w[0]['main']['humidity'], w[0]['wind']['speed']
        tomorrow = w[1]['weather'][0]['description'], w[1]['main']['temp'], w[1]['main']['humidity'], w[1]['wind']['speed']
        day3 = w[2]['weather'][0]['description'], w[2]['main']['temp'], w[2]['main']['humidity'], w[2]['wind']['speed']



        day4 = w[3]['weather'][0]['description'], w[3]['main']['temp'], w[3]['main']['humidity'], w[3]['wind']['speed']
        #day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['temp_max'], w[4]['main']['humidity'], w[4]['wind']['speed']
        day5 = w[4]['weather'][0]['description'], w[4]['main']['temp'], w[4]['main']['humidity'], w[4]['wind']['speed']

        day6 = w[5]['weather'][0]['description'], w[5]['main']['temp'], w[5]['main']['humidity'], w[5]['wind']['speed']
        day7 = w[6]['weather'][0]['description'], w[6]['main']['temp'], w[6]['main']['humidity'], w[6]['wind']['speed']
        day8 = w[7]['weather'][0]['description'], w[7]['main']['temp'], w[7]['main']['humidity'], w[7]['wind']['speed']

        day9 = w[8]['weather'][0]['description'], w[8]['main']['temp'], w[8]['main']['humidity'], w[8]['wind']['speed']
        day10 = w[9]['weather'][0]['description'], w[9]['main']['temp'], w[9]['main']['humidity'], w[9]['wind']['speed']
        day11 = w[10]['weather'][0]['description'], w[10]['main']['temp'], w[10]['main']['humidity'], w[10]['wind']['speed']

        day12 = w[11]['weather'][0]['description'], w[11]['main']['temp'], w[11]['main']['humidity'], w[11]['wind']['speed']
        day13 = w[12]['weather'][0]['description'], w[12]['main']['temp'], w[12]['main']['humidity'], w[12]['wind']['speed']
        day14 = w[13]['weather'][0]['description'], w[13]['main']['temp'], w[13]['main']['humidity'], w[13]['wind']['speed']
        day15 = w[14]['weather'][0]['description'], w[14]['main']['temp'], w[14]['main']['humidity'], w[14]['wind']['speed']

       # return weather['city']['name'], current, tomorrow, dayafter, currentt, tomorroww, dayafterr, dayafterr_, dayafterr__, day, day_,day__,today, today_,today__,today___#, currentt_, tomorroww_, dayafterr_
        return weather['city']['name'], current, tomorrow, day3, day4, day5, day6, day7, day8, day9, day10,day11,day12, day13,day14,day15

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

