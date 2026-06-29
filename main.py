import os
import requests

def get_weather(city="Ottawa"):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        today = data['weather'][0]
        hourly = today['hourly']
        
        # 统计今天的总降水量和最大降水概率
        precip = sum(float(h.get('precipMM', 0)) for h in hourly)
        chance_of_rain = max(int(h.get('chanceofrain', 0)) for h in hourly)
        conditions = hourly[4]['weatherDesc'][0]['value'] # 选取中午的天气情况作为代表
        
        return (f"**📍 {city}**\n"
                f"🌡️ 气温: {today['mintempC']}°C ~ {today['maxtempC']}°C\n"
                f"☀️ 天气: {conditions}\n"
                f"💧 降水: {chance_of_rain}% ({precip:.1f}mm)")
    except Exception as e:
        return f"获取 {city} 天气失败: {e}"

def push_to_discord(weather_text):
    # 从环境变量中读取 Webhook URL，保证安全
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("错误：未找到 DISCORD_WEBHOOK_URL 环境变量")
        return

    data = {
        "content": f"🌤️ **早安！今日天气播报：**\n\n{weather_text}"
    }
    
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("推送成功！")
    else:
        print(f"推送失败，状态码: {response.status_code}")

if __name__ == "__main__":
    weather_ottawa = get_weather("Ottawa")
    weather_sudbury = get_weather("Sudbury")
    push_to_discord(f"{weather_ottawa}\n\n{weather_sudbury}")