import sqlite3

# Connect (or create) SQLite database
conn = sqlite3.connect("aviation_flights.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS flights (
    date TEXT,
    status TEXT,
    flight_code TEXT,
    airline TEXT,
    departure_airport TEXT,
    departure_scheduled TEXT,
    arrival_airport TEXT,
    arrival_scheduled TEXT,
    arrival_delay INTEGER
)
""")
conn.commit()
conn.close()

print("Database 'aviation_flights.db' and table 'flights' created successfully!")
