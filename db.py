import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_PASSWORD = os.getenv('DB_PASSWORD')


conn = psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_HOST, 
        port=DB_PORT
    )
print("Successful connected")
cur = conn.cursor()

def init_table():

    # Создаем таблицу running_statistics, если ее нет
    cur.execute('''
    CREATE TABLE IF NOT EXISTS running_statistics (
        id SERIAL PRIMARY KEY,
        kilometers FLOAT,
        minutes INTEGER,
        date DATE
    )
''')
    conn.commit()

def create_record(km, minutes,date):
    cur.execute('''
    INSERT INTO running_statistics (kilometers, minutes,date)
    VALUES (%s, %s,%s)
    ''', (km, minutes,date))
    conn.commit()
    print("Record created successfully")


def read_all_records():
    cur.execute('SELECT * FROM running_statistics')
    rows = cur.fetchall()
    
    print("{:<5} {:<10} {:<10} {:<10}".format('ID', 'Kilometers', 'Minutes', 'Date'))
    print("-" * 45)
    
    for row in rows:
        row_data = [str(val) if val is not None else "N/A" for val in row]
        print("{:<5} {:<10} {:<10} {:<10}".format(*row_data))


init_table()
#minutes = 30
#date = "2024-06-03"
#create_record (kilometers, minutes, date)
read_all_records()
