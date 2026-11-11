import os
import requests
import pandas as pd
import numpy as np
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
    "facets[type][]": "D",                        # D = demand
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

df = pd.DataFrame(rows)
#print(df.columns)
# Differentiating between 'Demand' and 'Demand Forecast' based off of "type"

# Which hour of the day has the highest average demand?

# Sort dataset by hour of the day
# Time Stamps are 24 hours (tt - TT) 
# formatted 2026-11-01(tt), need to remove first

df_hours = df.copy()

df_hours['Hour'] = df_hours['period'].str.split('T').str[1]

# Now have Time of Day column, average out values by Time of Day
df_hours['value'] = df['value'].astype(int)
x = df_hours.groupby(['Hour'])['value'].mean()

# Better approach would be to work with TimeZone directly :

df_timezone = df.copy()

df_timezone['Date Time'] = pd.to_datetime(df_timezone['period'], utc = 'True').dt.tz_convert('America/Chicago')
df_timezone['value'] = pd.to_numeric(df_timezone['value'], errors = 'coerce').astype('Int64')
df_timezone['Time of Day'] = df_timezone['Date Time'].dt.hour

y = df_timezone.groupby(df_timezone['Time of Day'])['value'].mean()

y1 = y.idxmax()

# What was the peak demand hour of the week?

z = df_timezone.loc[df_timezone['value'].idxmax()]

#print(z)

#How does a weekday compare with the weekend?

#Convert 'period' to day of the week

df_timezone['Day of the Week'] = df_timezone['Date Time'].dt.day_of_week

df_timezone['Week.End'] = np.where((df_timezone['Day of the Week'] == 5) | (df_timezone['Day of the Week'] == 6), 'Weekend', "Weekday")

t = df_timezone.groupby(df_timezone['Week.End'])['value'].mean()

d = df_timezone.groupby(df_timezone['Day of the Week'])['value'].mean()

print(t)