import os
import requests

def get_weather_data(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        today = data['weather'][0]
        tomorrow = data['weather'][1]
        hourly = today['hourly']
        
        precip = sum(float(h.get('precipMM', 0)) for h in hourly)
        
        # 辅助函数：找出降水（雨或雪）概率最大的一段
        def get_max_precip(hourly_data):
            def max_chance(h):
                return max(int(h.get('chanceofrain', 0)), int(h.get('chanceofsnow', 0)))
            max_hour = max(hourly_data, key=max_chance)
            return max_chance(max_hour), max_hour

        # 今天的降水概率与天气状况
        chance_of_precip, max_precip_hour = get_max_precip(hourly)
        if chance_of_precip >= 30:
            conditions = max_precip_hour['weatherDesc'][0]['value']
        else:
            conditions = hourly[4]['weatherDesc'][0]['value'] # 默认中午
            
        # 明天的降水概率与天气状况
        tomorrow_chance, tomorrow_max_hour = get_max_precip(tomorrow['hourly'])
        if tomorrow_chance >= 30:
            tomorrow_cond = tomorrow_max_hour['weatherDesc'][0]['value']
        else:
            tomorrow_cond = tomorrow['hourly'][4]['weatherDesc'][0]['value']

        # 获取全天最高体感温度，而不是脚本执行当时的体感温度
        feels_like = max(int(h['FeelsLikeC']) for h in hourly)
        uv_index = int(today.get('uvIndex', 0))
        
        tomorrow_min = tomorrow['mintempC']
        tomorrow_max = tomorrow['maxtempC']
        
        # 智能提示
        tips = []
        if chance_of_precip > 50 or precip > 2.0:
            if int(max_precip_hour.get('chanceofsnow', 0)) > 50:
                tips.append("❄️ 提醒：今天大概率会下雪，出门注意防寒防滑！")
            else:
                tips.append("☔ 提醒：今天大概率会下雨，出门别忘了带伞哦！")
        
        if int(today['maxtempC']) >= 30 or feels_like >= 35:
            tips.append("🔥 提醒：天气炎热，注意防暑降温！")
        if uv_index > 5:
            tips.append("🕶️ 提醒：今天紫外线较强，注意防晒！")
        if int(today['mintempC']) < 5 or (int(today['maxtempC']) - int(today['mintempC']) > 15):
            tips.append("🧥 提醒：气温较低或昼夜温差大，注意保暖！")
            
        tip_text = "\n".join(tips) if tips else "🌤️ 今天气温适宜，是不错的一天！"

        # 判断颜色 (比如下雨蓝色，晴天橙色，多云灰色，下雪白色)
        color = 0xFFA500 # 默认橙色 (晴天)
        if chance_of_precip > 50 or precip > 1.0:
            if "snow" in conditions.lower() or int(max_precip_hour.get('chanceofsnow', 0)) > 50:
                color = 0xECF0F1 # 白色/浅蓝
            else:
                color = 0x3498DB # 蓝色
        elif "cloud" in conditions.lower() or "overcast" in conditions.lower():
            color = 0x95A5A6 # 灰色

        embed = {
            "title": f"📍 {city} 今日天气",
            "color": color,
            "fields": [
                {"name": "🌡️ 气温与体感", "value": f"{today['mintempC']}°C ~ {today['maxtempC']}°C (最高体感 {feels_like}°C)", "inline": True},
                {"name": "☀️ 天气状况", "value": f"{conditions} (UV指数: {uv_index})", "inline": True},
                {"name": "💧 降水概率", "value": f"{chance_of_precip}% (约 {precip:.1f}mm)", "inline": True},
                {"name": "🔮 明日预报", "value": f"{tomorrow_cond}, {tomorrow_min}°C ~ {tomorrow_max}°C", "inline": False},
                {"name": "💡 出行建议", "value": tip_text, "inline": False}
            ]
        }
        return embed
    except Exception as e:
        return {
            "title": f"📍 {city} 天气获取失败",
            "description": str(e),
            "color": 0xE74C3C
        }

def push_to_discord(embeds):
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("错误：未找到 DISCORD_WEBHOOK_URL 环境变量")
        return

    data = {
        "content": "🌤️ **早安！今日天气播报：**",
        "embeds": embeds
    }
    
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("推送成功！")
    else:
        print(f"推送失败，状态码: {response.status_code}")

if __name__ == "__main__":
    # 从环境变量中读取城市，默认是 Ottawa,Sudbury
    cities_env = os.environ.get("CITIES", "Ottawa,Sudbury")
    cities = [c.strip() for c in cities_env.split(",") if c.strip()]
    
    embeds = []
    for city in cities:
        embeds.append(get_weather_data(city))
        
    if embeds:
        push_to_discord(embeds)