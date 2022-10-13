import sqlite3
import weather
import datetime

try:
    conn = sqlite3.connect('WeatherDB.db') #creating database connection
    print("Połączono")

except Exception as e:
    print("Error", str(e))
        
def InsertWindSpeed(WindSpeed,Winddeg,Temperature):
    try:
        
        val1 = (WindSpeed,Winddeg,Temperature)
        
        cur = conn.cursor()
        sql = "INSERT INTO Wind (SpeedOfWind,DegreeOfWind,Temperature) VALUES(?,?,?)" #Adding values of speed and angle of wind to database 
        cur.execute(sql,val1) #executing sql insert with values from api 
        conn.commit() #executing sql insert with values from api 
        
    except Exception as e:
        print(e)
     
def InsertDate():
    try:
        # using now() to get current time
        current_time = datetime.datetime.now()

        # Attributes of now()
        CurrentDay = current_time.day
        CurrentMonth = current_time.month
        CurrentYear = current_time.year
        Date = (CurrentDay,CurrentMonth,CurrentYear)

        #Inserting Date to Database
        cur = conn.cursor()
        sql =  "INSERT INTO Date (Day, Month, Year) VALUES(?,?,?)"
        cur.execute(sql,Date)
        conn.commit() #executing sql insert with values from api 

    except Exception as e:
        print(e)

InsertWindSpeed(weather.SpeedOfWind,weather.DegreeOfWind,weather.Temperature)
InsertDate()
conn.close()