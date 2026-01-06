import sqlite3
import pandas as pd

conn = sqlite3.connect("aviation_flights.db")
df = pd.read_sql("SELECT * FROM flights", conn)
conn.close()

print(df) 


