import sqlite3 #Importing sqlite3
from sqlite3 import Error #Importing Error from sqlite3

database = r"Weather.db" #Creating database

def create_connection(db_file):
    """ create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn #Returns connection

def SelectTemperature(conn):
    """
    Select Speed of angle of wind and pass it to table
    """
    TemperatureTable = [] #Creating table for temperature

    cur = conn.cursor() 
    cur.execute("SELECT Temperature FROM Wind") #Selecting Temperature from database

    rows = cur.fetchall() #Fetching data from database

    for row in rows:
        TemperatureTable.append(row[0]) #Adding temperature to table

    cur.close()
    
    return TemperatureTable #Returns table with temperature

def SelectSpeed(conn):
    """
    Select Speed of wind and pass it to table
    """
    
    SpeedOfWindTable = [] #Creating table for speed of wind

    cur = conn.cursor()
    cur.execute("SELECT SpeedOfWind FROM Wind") #Selecting Speed of wind from database

    rows = cur.fetchall() #Fetching data from database

    for row in rows:
        SpeedOfWindTable.append(row[0]) #Adding speed of wind to table

    cur.close()
    return SpeedOfWindTable

def SelectAngle(conn):
    """
    Select Speed of angle of wind and pass it to table
    """
    
    WindDegreeTable = []
    
    cur = conn.cursor()
    cur.execute("SELECT DegreeOfWind FROM Wind") #Selecting Degree of wind from database

    rows = cur.fetchall() #Fetching data from database

    for row in rows: 
        WindDegreeTable.append(row[0]) #Adding angle of wind to table

    cur.close() 
    return WindDegreeTable 

def SelectDate(conn):
    """
    Select Speed of angle of wind and pass it to table
    """
    
    DateTable = []
    
    cur = conn.cursor() 
    cur.execute("SELECT Today FROM Date") #Selecting Date from database

    rows = cur.fetchall()

    for row in rows:
       DateTable.append(row[0]) #Adding Date to table

    cur.close()
    
    print (DateTable) #Prints date table
    return DateTable #Returns date table

TableTemperature= SelectTemperature(create_connection(database)) #temperature in Warsaw
TableSpeed = SelectSpeed(create_connection(database)) #speed of wind in Warsaw
TableDegree= SelectAngle(create_connection(database)) #degree of wind
TableDate = SelectDate(create_connection(database)) #date