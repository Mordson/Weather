import sqlite3
import weather

try:
    conn = sqlite3.connect('WeatherDB.db') #creating database connection
    print("Połączono")

except Exception as e:
    print("Error", str(e))
        

def InsertWindSpeed(WindSpeed,Winddeg):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO Wind (ID,SpeedOfWind,Angle) VALUES(' ',3,3)' #Adding values of speed and angle of wind to database 
        cur.execute(sql)
        conn.commit()
        conn.close()
        
    except Exception as e:
        print(e)
     
InsertWindSpeed(weather.WindSpeed,weather.WindDegree)