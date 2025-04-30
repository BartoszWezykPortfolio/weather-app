from datetime import datetime

current_time = datetime.now()
time = current_time.time()
date = current_time.date()

def logs_successfull():
    with open('log.txt', 'w') as my_file:
        my_file.write(f'{date}-{time} Pobrano dane pogodowe')

    print('Log file has been successfully saved')

def logs_failed():
    with open('log.txt', 'w') as my_file:
        my_file.write(f'{date}-{time} Nie udało się pobrać danych')

    print('Log file has been successfully saved')

def logs_read():
    with open('log.txt') as my_file:
        print(my_file.read())