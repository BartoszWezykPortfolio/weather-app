from pymongo import MongoClient
from config import Config

# def db():
#     client = MongoClient(Config.DB_URI)
#     db = client['cities_db']
#     collection = db['WeatherData_test']
#
#     return collection

def save_to_mongo(collection, data):
    try:
        collection.insert_one(data)
        print('Dane zostały przesłane do bazy')
    except Exception as e:
        print(e)