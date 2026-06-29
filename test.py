import requests

r = requests.get("https://wttr.in/Ottawa?format=j1")
data = r.json()

today = data['weather'][0]
hourly = today['hourly']
precip = sum(float(h.get('precipMM', 0)) for h in hourly)
chance_of_rain = max(int(h.get('chanceofrain', 0)) for h in hourly)
conditions = hourly[4]['weatherDesc'][0]['value'] # Noon

print(f"🌡️ {today['mintempC']}°C - {today['maxtempC']}°C")
print(f"💧 降水概率: {chance_of_rain}% (约 {precip:.1f}mm)")
print(f"☀️ 白天天气: {conditions}")
