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
        "push_failed": "Push failed, status code: {code}",
        "alert_smoke": "⚠️ ALERT: Smoke/Wildfire detected. Air quality may be poor!",
        "alert_freezing_rain": "⚠️ ALERT: Freezing rain. Roads will be extremely slippery!",
        "alert_storm": "⚠️ ALERT: Severe storm/thunderstorm approaching.",
        "alert_blizzard": "⚠️ ALERT: Blizzard/Heavy snow conditions."
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
        "push_failed": "推送失败，状态码: {code}",
        "alert_smoke": "⚠️ 警报：检测到烟尘/山火！空气质量可能很差，请注意防范！",
        "alert_freezing_rain": "⚠️ 警报：冻雨天气！道路将极度结冰湿滑，请小心出行！",
        "alert_storm": "⚠️ 警报：暴风雨/雷暴天气即将来临，请注意安全！",
        "alert_blizzard": "⚠️ 警报：暴风雪/大雪天气，视线不佳且路面积雪，请尽量减少外出！"
    }
}

def get_text(lang, key, **kwargs):
    # Default to 'zh' if lang is not found, fallback to key if key not found
    text_dict = I18N.get(lang, I18N["zh"])
    text = text_dict.get(key, I18N["en"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text

WMO_CODES = {
    "en": {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        56: "Light freezing drizzle", 57: "Dense freezing drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        66: "Light freezing rain", 67: "Heavy freezing rain",
        71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
    },
    "zh": {
        0: "晴朗",
        1: "大部晴朗", 2: "局部多云", 3: "阴天",
        45: "有雾", 48: "雾凇",
        51: "小毛毛雨", 53: "中毛毛雨", 55: "大毛毛雨",
        56: "小冻毛毛雨", 57: "大冻毛毛雨",
        61: "小雨", 63: "中雨", 65: "大雨",
        66: "小冻雨", 67: "大冻雨",
        71: "小雪", 73: "中雪", 75: "大雪",
        77: "米雪",
        80: "小阵雨", 81: "中阵雨", 82: "强阵雨",
        85: "小阵雪", 86: "大阵雪",
        95: "雷暴", 96: "雷暴伴有小冰雹", 99: "雷暴伴有大冰雹"
    }
}

def get_wmo_text(lang, code):
    lang_dict = WMO_CODES.get(lang, WMO_CODES['en'])
    return lang_dict.get(code, WMO_CODES['en'].get(code, 'Unknown'))
