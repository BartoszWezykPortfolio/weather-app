import os
import time
from pprint import pprint
from services.logs import logs_successfull, logs_failed, logs_read
from services.excel_file import save_to_excel
from services.get_weather_data import get_weather_data
from config import Config

def start():
    weather = get_weather_data(Config.API_KEY, Config.CITY)
    # pprint(list(weather.values()))
    # pprint(list(weather.keys()))
    logs_successfull()

    save_to_excel(Config.EXCEL_FILENAME, weather)

while True:
    try:
        start()
        print('Data loaded')
    except Exception as e:
        print(e)
        logs_failed()

    logs_read()
    time.sleep(3600)

