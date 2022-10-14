import sqlite3
import weather
import datetime

try:
    conn = sqlite3.connect('Weather.db') #creating database connection
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
        CurrentDay = str(current_time.day)
        CurrentMonth = str(current_time.month)
        CurrentYear = str(current_time.year)
        
        StringDate = (CurrentYear + "-" + CurrentMonth + "-" + CurrentDay)
 
        #Inserting Date to Database
        cur = conn.cursor()
        sql =  "INSERT INTO Date(Today) VALUES(?)"
        cur.execute(sql,[StringDate])
        conn.commit() #executing sql insert with values from api 

    except Exception as e:
        print(e)

InsertWindSpeed(weather.SpeedOfWind,weather.DegreeOfWind,weather.Temperature)
InsertDate()
conn.close()