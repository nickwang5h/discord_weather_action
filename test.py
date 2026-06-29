import requests
import json

r = requests.get("https://wttr.in/Ottawa?format=j1")
data = r.json()

current = data['current_condition'][0]
print(f"Current Feels Like: {current['FeelsLikeC']}C")

today = data['weather'][0]
print(f"Today UV: {today['uvIndex']}")

tomorrow = data['weather'][1]
print(f"Tomorrow Min: {tomorrow['mintempC']}, Max: {tomorrow['maxtempC']}")
print(f"Tomorrow Conditions: {tomorrow['hourly'][4]['weatherDesc'][0]['value']}")

