import os
import requests

def get_weather(city="Ottawa"):
    # 使用 wttr.in 的 format=4 可以返回一行极其简洁的天气概览
    # 例如: "Ottawa: ⛅️  +22°C ↙11km/h"
    url = f"https://wttr.in/{city}?format=4"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"获取天气失败: {e}"

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
    weather = get_weather()
    push_to_discord(weather)