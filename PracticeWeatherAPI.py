"""
URL request to a public Weather Forecast API (Oprn-Meteo)
Receives following categories:
latitude 
longitude 
generationtime_ms 
utc_offset_seconds 
timezone 
timezone_abbreviation 
elevation 
current_weather {'temperature','windspeed','winddirection','weathercode','time'}
daily_units
daily (next 7 days starting from date requested, including 'sunrise' and 'sunset' times)
format: YYYY-MM-DD-THH:MM with HH:MM in military time
"""

import requests
api_url = "https://api.open-meteo.com/v1/forecast?latitude=33.45&longitude=-112.07&daily=weathercode,sunrise,sunset&current_weather=true&temperature_unit=fahrenheit&timezone=auto"
response = requests.get(api_url)
jsonResponse = response.json()

# print(response.text)
print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)
