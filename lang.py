I18N = {
    "en": {
        "snow_tip": "❄️ Tip: High chance of snow today. Keep warm and beware of slippery roads!",
        "rain_tip": "☔ Tip: High chance of rain today. Don't forget your umbrella!",
        "hot_tip": "🔥 Tip: It's going to be hot. Stay hydrated and cool!",
        "uv_tip": "🕶️ Tip: High UV index today. Don't forget sunscreen!",
        "cold_tip": "🧥 Tip: Cold weather or large temperature difference today. Dress warmly!",
        "nice_tip": "🌤️ Nice weather today. Have a great day!",
        "weather_today": "📍 {city} Weather Today",
        "temp_feels_like": "🌡️ Temperature & Feels Like",
        "temp_value": "{min}°C ~ {max}°C (Max Feels Like {feels}°C)",
        "conditions": "☀️ Conditions",
        "conditions_value": "{cond} (UV Index: {uv})",
        "precip_chance": "💧 Precipitation Chance",
        "precip_value": "{chance}% (Approx. {precip:.1f}mm)",
        "tomorrow_forecast": "🔮 Tomorrow's Forecast",
        "tomorrow_value": "{cond}, {min}°C ~ {max}°C",
        "tips": "💡 Tips",
        "failed_title": "📍 Failed to fetch weather for {city}",
        "env_error": "Error: DISCORD_WEBHOOK_URL environment variable not found",
        "morning_greet": "🌤️ **Good morning! Here is today's weather forecast:**",
        "push_success": "Pushed successfully!",
        "push_failed": "Push failed, status code: {code}"
    },
    "zh": {
        "snow_tip": "❄️ 提醒：今天大概率会下雪，出门注意防寒防滑！",
        "rain_tip": "☔ 提醒：今天大概率会下雨，出门别忘了带伞哦！",
        "hot_tip": "🔥 提醒：天气炎热，注意防暑降温！",
        "uv_tip": "🕶️ 提醒：今天紫外线较强，注意防晒！",
        "cold_tip": "🧥 提醒：气温较低或昼夜温差大，注意保暖！",
        "nice_tip": "🌤️ 今天气温适宜，是不错的一天！",
        "weather_today": "📍 {city} 今日天气",
        "temp_feels_like": "🌡️ 气温与体感",
        "temp_value": "{min}°C ~ {max}°C (最高体感 {feels}°C)",
        "conditions": "☀️ 天气状况",
        "conditions_value": "{cond} (UV指数: {uv})",
        "precip_chance": "💧 降水概率",
        "precip_value": "{chance}% (约 {precip:.1f}mm)",
        "tomorrow_forecast": "🔮 明日预报",
        "tomorrow_value": "{cond}, {min}°C ~ {max}°C",
        "tips": "💡 出行建议",
        "failed_title": "📍 {city} 天气获取失败",
        "env_error": "错误：未找到 DISCORD_WEBHOOK_URL 环境变量",
        "morning_greet": "🌤️ **早安！今日天气播报：**",
        "push_success": "推送成功！",
        "push_failed": "推送失败，状态码: {code}"
    }
}

def get_text(lang, key, **kwargs):
    # Default to 'zh' if lang is not found, fallback to key if key not found
    text_dict = I18N.get(lang, I18N["zh"])
    text = text_dict.get(key, I18N["en"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text
