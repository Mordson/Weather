import sqlite3
import weather

try:
    conn = sqlite3.connect('WeatherDB.db')
    print("Połączono")

except Exception as e:
    print("error", str(e))
    
result = conn.execute("SELECT * FROM Temperature")

for row in result:
    print(row)

conn.close()