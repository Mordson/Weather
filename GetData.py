import sqlite3
from sqlite3 import Error

database = r"Weather.db"

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
    cur.execute("SELECT Temperature FROM Wind")

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
    cur.execute("SELECT DegreeOfWind FROM Wind")

    rows = cur.fetchall()

    for row in rows:
        WindDegreeTable.append(row[0])

    cur.close()
    return WindDegreeTable

TableTemperature= SelectTemperature(create_connection(database)) #temperature in Warsaw
TableSpeed = SelectSpeed(create_connection(database)) #speed of wind in Warsaw
TableDegree= SelectAngle(create_connection(database)) #degree of wind