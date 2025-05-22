import os
import sys
import time
from itertools import repeat

from pymongo import MongoClient
from services.logs import logs_successfull, logs_failed, logs_read
from services.excel_file import save_to_excel
from services.get_weather_data import get_weather_data
from services.mongodb import save_to_mongo
from services.mysql_connector import mysql_connect, mysql_select
from config import Config


repeat = 0

CITY = input('Podaj nazwę miasta\n')
OPERATION = int(input(
    'Wybierz akcję\n '
    '1. Zapisz do pliku .xlsx\n '
    '2. Zapisz do MongoDB\n '
    '3. Zapisz dane do bazy mysql\n '
    '4. Wyświetl 10 najnowszych rekordów z bazy mysql\n '
    '5. Zapisz do xlsx oraz bazy MongoDB'))

def generate_mysql_table_name(city):
    return f'{city.lower().replace(' ', '')}weatherdata'

mysql_table_name = generate_mysql_table_name(CITY)

def db_data(city):
    client = MongoClient(Config.DB_URI)
    db = client['cities_db']
    collection_name = f"{city.title().replace(' ', '')}WeatherData"
    collection = db[collection_name]

    return collection

def start():
    weather = get_weather_data(Config.API_KEY, CITY)
    # pprint(list(weather.values()))
    # pprint(list(weather.keys()))
    logs_successfull()

    coll = db_data(CITY)

    match OPERATION:
        case 1:
            save_to_excel(Config.EXCEL_FILENAME, weather)
        case 2:
            save_to_mongo(coll, weather)
        case 3:
            mysql_connect(weather, mysql_table_name)
        case 4:
            mysql_select(mysql_table_name)
            sys.exit()
        case 5:
            save_to_excel(Config.EXCEL_FILENAME, weather)
            save_to_mongo(coll, weather)
        case _:
            print('Brak wybranej akcji')

while repeat < 5:
    try:
        start()
        print('Data loaded')
        repeat += 1
    except Exception as e:
        print(e)
        logs_failed()

    logs_read()
    time.sleep(10)

