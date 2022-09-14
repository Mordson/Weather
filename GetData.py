import sqlite3
from sqlite3 import Error

database = r"WeatherDB.db"

TemperatureTable = []
SpeedOfWindTable = []
WindDegreeTable = []

def create_connection(db_file):
    """ create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def SelectTemperature(conn):
    """
    Select Speed of angle of wind and pass it to table
    """
    TemperatureTable = []

    cur = conn.cursor()
    cur.execute("SELECT Temperature FROM Temperature")

    rows = cur.fetchall()

    for row in rows:
        TemperatureTable.append(row[0])

    cur.close()
    
    return TemperatureTable

def SelectSpeed(conn):
    """
    Select Speed of wind and pass it to table
    """
    
    SpeedOfWindTable = []

    cur = conn.cursor()
    cur.execute("SELECT SpeedOfWind FROM Wind")

    rows = cur.fetchall()

    for row in rows:
        SpeedOfWindTable.append(row[0])

    cur.close()
    
    return SpeedOfWindTable

def SelectAngle(conn):
    """
    Select Speed of angle of wind and pass it to table
    """
    
    WindDegreeTable = []
    
    cur = conn.cursor()
    cur.execute("SELECT Angle FROM Wind")

    rows = cur.fetchall()

    for row in rows:
        WindDegreeTable.append(row[0])

    cur.close()

    return WindDegreeTable