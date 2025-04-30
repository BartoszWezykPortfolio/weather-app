import os
from pprint import pprint
from dotenv import load_dotenv
from services.logs import logs_successfull, logs_failed, logs_read
from services.get_weather_data import get_weather_data

load_dotenv()

API_KEY = os.environ.get('API_KEY')
CITY = os.environ.get('CITY')

try:
    weather = get_weather_data(API_KEY, CITY)
    pprint(weather)
    logs_successfull()
except Exception as e:
    print(e)
    logs_failed()

logs_read()