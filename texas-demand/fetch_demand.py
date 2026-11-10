import os
import requests
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
    "facets[type][]": "D",            # D = demand
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
print(f"Got {len(rows)} hours of data")

for row in rows[:5]:
    print(row["period"], row["value"], row["value-units"])
