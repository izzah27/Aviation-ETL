import requests
import pandas as pd
import sqlite3

# ----------------------------
# 1. Extract
# ----------------------------
API_KEY = "b0d243e3222ccaa8a3a7972b9c5c134b"
URL = "http://api.aviationstack.com/v1/flights"

params = {
    "access_key": API_KEY,
    "limit": 50,
    "airline_iata": "MH"
}

response = requests.get(URL, params=params)
data = response.json()

if "data" not in data:
    print("No data received. Full response:", data)
    exit()

flights = data["data"]

# ----------------------------
# 2. Transform
# ----------------------------
flat_flights = []
for f in flights:
    flat_flights.append({
        "date": f.get("flight_date"),
        "status": f.get("flight_status"),
        "flight_code": f.get("flight", {}).get("iata"),
        "airline": f.get("airline", {}).get("name"),
        "departure_airport": f.get("departure", {}).get("airport"),
        "departure_scheduled": f.get("departure", {}).get("scheduled"),
        "arrival_airport": f.get("arrival", {}).get("airport"),
        "arrival_scheduled": f.get("arrival", {}).get("scheduled"),
        "arrival_delay": f.get("arrival", {}).get("delay")
    })

df = pd.DataFrame(flat_flights)

# ----------------------------
# 3. Load to SQLite
# ----------------------------
conn = sqlite3.connect("aviation_flights.db")  # use the database we created
df.to_sql("flights", conn, if_exists="append", index=False)
conn.close()

print("\nSaved 50 flights to SQLite database 'aviation_flights.db'")
