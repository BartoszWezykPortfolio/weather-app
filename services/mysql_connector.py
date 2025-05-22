from config import Config
import mysql.connector as mysql


def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        temp DECIMAL(5, 2) NOT NULL,
        temp_feels DECIMAL(5, 2) NOT NULL,
        humidity INT NOT NULL,
        wind_speed DECIMAL(5, 2) NOT NULL,
        date DATE NOT NULL,
        time_added TIME NOT NULL
        )
    """
    cursor.execute(create_table_query)

def mysql_connect(weather):
    mysql_config = {
        'user':Config.MYSQL_USER,
        'password':Config.MYSQL_PASS,
        'host':Config.MYSQL_HOST,
        'database':Config.MYSQL_BD
    }

    try:
        conn = mysql.connect(**mysql_config)
        cursor = conn.cursor()
        create_table(cursor)

        insert_sql = """
            INSERT INTO weather (name, temp, temp_feels, humidity, wind_speed, date, time_added) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_sql, tuple(weather.values()))
        conn.commit()
        print('Dodano dane pogodowe do bazy')

    except Exception as e:
        print(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Zamknięto połączenie')

