import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    API_KEY = os.environ.get('API_KEY')
    CITY = os.environ.get('CITY')
    LOG_FILENAME = 'logs.txt'
    EXCEL_FILENAME = r'C:\Users\Bartosz\PycharmProjects\WeatherAPI\Weather_data.xlsx'