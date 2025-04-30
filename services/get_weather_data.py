from http.client import responses

import requests
from pprint import pprint
from utils.temp_converter import kelvin_to_celsius
from utils.wind_converter import ms_to_kmh
from utils.date_converter import date_format
import time

def get_weather_data(token: str, city: str):

    timestamp = time.strftime('%H:%M')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

    try:
        response = requests.get(url)
        data = response.json()

        weather = {
            'Name': data['name'],
            'Temp': kelvin_to_celsius(data['main']['temp']),
            'Temp_Feels': kelvin_to_celsius(data['main']['feels_like']),
            'Humidity': data['main']['humidity'],
            'Wind_Speed': ms_to_kmh(data['wind']['speed']),
            'Date': date_format(data['dt']),
            'Time_Added': timestamp
        }

        return weather
    except Exception as e:
        print(e)