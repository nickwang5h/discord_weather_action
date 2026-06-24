import os
import requests

def get_weather(city="Ottawa"):
    # 使用自定义 format 获取包含降水量(%p)等更多信息的天气
    # %l: 城市名, %c: 天气emoji, %t: 温度, %p: 降水量(mm), %w: 风速和方向, %h: 湿度
    url = f"https://wttr.in/{city}"
    params = {
        "format": "%l: %c %t 💧%p 💨%w 💦%h",
        "m": ""
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"获取 {city} 天气失败: {e}"

def push_to_discord(weather_text):
    # 从环境变量中读取 Webhook URL，保证安全
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("错误：未找到 DISCORD_WEBHOOK_URL 环境变量")
        return

    data = {
        "content": f"🌤️ **早安！今日天气播报：**\n> {weather_text}"
    }
    
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("推送成功！")
    else:
        print(f"推送失败，状态码: {response.status_code}")

if __name__ == "__main__":
    weather_ottawa = get_weather("Ottawa")
    weather_sudbury = get_weather("Sudbury")
    push_to_discord(f"{weather_ottawa}\n> {weather_sudbury}")