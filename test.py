import requests
import json

r = requests.get("https://wttr.in/Ottawa?format=j1")
data = r.json()

today = data['weather'][0]
hourly = today['hourly']

max_rain_hour = max(hourly, key=lambda h: int(h.get('chanceofrain', 0)))
chance_of_rain = int(max_rain_hour.get('chanceofrain', 0))

if chance_of_rain >= 30:
    conditions = max_rain_hour['weatherDesc'][0]['value']
else:
    conditions = hourly[4]['weatherDesc'][0]['value']

print("Condition:", conditions, "Chance:", chance_of_rain)


