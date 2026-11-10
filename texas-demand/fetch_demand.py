import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("EIA_API_KEY")

# Where the data lives, and what we're asking for
url = "https://api.eia.gov/v2/electricity/rto/region-data/data/"
params = {
    "api_key": api_key,
    "frequency": "hourly",
    "data[0]": "value",
    "facets[respondent][]": "ERCO",   # ERCOT's code at EIA
    "facets[type][]": ["D", 'DF'],                        # D = demand
    "start": "2026-11-01T00",
    "end": "2026-11-08T00",
    "sort[0][column]": "period",
    "sort[0][direction]": "asc",
    "length": 5000,
}

# Ask the API for the data
response = requests.get(url, params=params)
response.raise_for_status()   # stop with an error if the request failed
data = response.json()

# Dig into the response and print the first few hours
rows = data["response"]["data"]
#print(f"Got {len(rows)} hours of data")

# Differentiating between 'Demand' and 'Demand Forecast' based off of "type"

demand_rows = []
forecast_rows = []

for row in rows[:]:
    if row['type'] == 'D':
        demand_rows.append(row)
    elif row['type'] == "DF":
        forecast_rows.append(row)

# Find out if "values" column contains str (text) or integers/values

# print(type(demand_rows[0]['value']))
#print(len(demand_rows), len(forecast_rows))
# Cells in "values" column contain str, must convert via int() or float() during calculation

# define forecast dictionary and assign keys -> assigning keys prevents the previous addition from being overwritten by the next addition 

forecast_by_period = {}
timestamp = 'period'
value = 'value'

for forecast_row in forecast_rows:
    forecast_by_period[forecast_row[timestamp]] = int(forecast_row[value])

differences = []

for demand_row in demand_rows:
    match_val = demand_row[timestamp]

    if match_val in forecast_by_period:
        difference = int(demand_row[value]) - forecast_by_period[match_val]

    differences.append({timestamp: match_val, "result": difference})


total = 0
for item in differences:
    total = total + item['result']

average = total / len(differences)

print (average)
# Finding the maximum value of Demand

# max_row = max(rows, key=lambda row:row['value'])

# print(max_row)

#for row in rows[:169]:
    #print(row["period"], row["value"], row["value-units"])
