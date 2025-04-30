from datetime import datetime
from config import Config


current_time = datetime.now()
time = current_time.time()
date = current_time.date()

def logs_successfull():
    with open(Config.LOG_FILENAME, 'w',encoding='utf8') as my_file:
        my_file.write(f'{date}-{time} Pobrano dane pogodowe')

    print('Log file has been successfully saved')

def logs_failed():
    with open(Config.LOG_FILENAME, 'w',encoding='utf8') as my_file:
        my_file.write(f'{date}-{time} Nie udało się pobrać danych')

    print('Log file has been successfully saved')

def logs_read():
    with open(Config.LOG_FILENAME,encoding='utf8') as my_file:
        print(my_file.read())