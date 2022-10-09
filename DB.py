import sqlite3
import weather

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
        conn.close()
        
    except Exception as e:
        print(e)
     
InsertWindSpeed(weather.SpeedOfWind,weather.DegreeOfWind,weather.Temperature)