import sqlite3
from sqlite3 import Error

database = r"WeatherDB.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def SelectSpeedAngle(conn):
    """
    Select Speed of wind and angle of wind
    """
    cur = conn.cursor()
    cur.execute("SELECT SpeedOfWind, Angle FROM Wind")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():

    # create a database connection
    conn = create_connection(database)
    with conn:
        SelectSpeedAngle(conn)


if __name__ == '__main__':
    main()