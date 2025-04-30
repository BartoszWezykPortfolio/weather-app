from http.client import responses

import requests
from pprint import pprint
from utils.temp_converter import kelvin_to_celsius
from utils.wind_converter import ms_to_kmh

def get_weather_data(token: str, city: str):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

    try:
        response = requests.get(url)
        data = response.json()

        weather = {
            'name': data['name'],
            'temp': kelvin_to_celsius(data['main']['temp']),
            'temp_feels': kelvin_to_celsius(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'wind_speed': ms_to_kmh(data['wind']['speed']),
            'date': data['dt']
        }

        return weather
    except Exception as e:
        print(e)