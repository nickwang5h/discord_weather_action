import requests
params = {"format": "%l: %c %t 💧%p 💨%w 💦%h", "m": ""}
r = requests.get("https://wttr.in/Ottawa", params=params)
print(r.text.strip())
