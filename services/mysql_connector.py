from config import Config
import mysql.connector as mysql
from utils.date_converter import time_format


def create_table(cursor, mysql_table_name):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS `{mysql_table_name}` (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        temp FLOAT NOT NULL,
        temp_feels FLOAT NOT NULL,
        humidity INT NOT NULL,
        wind_speed FLOAT NOT NULL,
        date VARCHAR(15) NOT NULL,
        time_added TIME NOT NULL
        )
    """
    cursor.execute(create_table_query)

def mysql_connect(weather, mysql_table_name):
    mysql_config = {
        'user':Config.MYSQL_USER,
        'password':Config.MYSQL_PASS,
        'host':Config.MYSQL_HOST,
        'database':Config.MYSQL_BD
    }

    try:
        conn = mysql.connect(**mysql_config)
        cursor = conn.cursor()
        create_table(cursor, mysql_table_name)

        insert_sql = f"""
            INSERT INTO `{mysql_table_name}` (name, temp, temp_feels, humidity, wind_speed, date, time_added) 
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

def mysql_select(mysql_table_name):
    mysql_config = {
        'user':Config.MYSQL_USER,
        'password':Config.MYSQL_PASS,
        'host':Config.MYSQL_HOST,
        'database':Config.MYSQL_BD
    }

    try:
        conn = mysql.connect(**mysql_config)
        cursor = conn.cursor()

        select_sql = f"""
            SELECT * FROM `{mysql_table_name}`
            ORDER BY time_added DESC
            LIMIT 10
        """
        cursor.execute(select_sql)
        results = cursor.fetchall()

        for row in results:
            formatted = [time_format(v) for v in row]
            print(formatted)

    except Exception as e:
        print(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Zamknięto połączenie')