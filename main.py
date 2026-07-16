import os
import requests
from lang import get_text

# Default language to 'zh' (Chinese), can be changed via environment variable
LANGUAGE = os.environ.get("LANGUAGE", "zh").lower()

def get_weather_data(city):
    # Pass lang=zh if LANGUAGE is zh to get translated weather descriptions if wttr.in supports it,
    # though we still use the English weatherDesc for condition checks.
    url = f"https://wttr.in/{city}?format=j1"
    if LANGUAGE == 'zh':
        url += "&lang=zh"
        
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        today = data['weather'][0]
        tomorrow = data['weather'][1]
        hourly = today['hourly']
        
        precip = sum(float(h.get('precipMM', 0)) for h in hourly)
        
        # Helper function: Find the period with the highest precipitation (rain or snow) probability
        def get_max_precip(hourly_data):
            def max_chance(h):
                return max(int(h.get('chanceofrain', 0)), int(h.get('chanceofsnow', 0)))
            max_hour = max(hourly_data, key=max_chance)
            return max_chance(max_hour), max_hour

        # Today's precipitation probability and weather condition
        chance_of_precip, max_precip_hour = get_max_precip(hourly)
        
        # Helper to get the correct language description from the hour data
        def get_desc(hour_data):
            if LANGUAGE == 'zh' and 'lang_zh' in hour_data:
                return hour_data['lang_zh'][0]['value']
            return hour_data['weatherDesc'][0]['value']

        if chance_of_precip >= 30:
            conditions_en = max_precip_hour['weatherDesc'][0]['value']
            conditions_display = get_desc(max_precip_hour)
        else:
            conditions_en = hourly[4]['weatherDesc'][0]['value'] # Default to noon
            conditions_display = get_desc(hourly[4])
            
        # Tomorrow's precipitation probability and weather condition
        tomorrow_chance, tomorrow_max_hour = get_max_precip(tomorrow['hourly'])
        if tomorrow_chance >= 30:
            tomorrow_cond_display = get_desc(tomorrow_max_hour)
        else:
            tomorrow_cond_display = get_desc(tomorrow['hourly'][4])

        # Get the highest feels-like temperature of the day, not the feels-like temperature at the time of script execution
        feels_like = max(int(h['FeelsLikeC']) for h in hourly)
        uv_index = int(today.get('uvIndex', 0))
        
        tomorrow_min = tomorrow['mintempC']
        tomorrow_max = tomorrow['maxtempC']
        
        # Check for severe weather alerts from hourly descriptions
        alert_tips = []
        is_severe = False
        all_conds_str = " ".join([h['weatherDesc'][0]['value'].lower() for h in hourly])
        
        if "smoke" in all_conds_str or "haze" in all_conds_str or "wildfire" in all_conds_str:
            alert_tips.append(get_text(LANGUAGE, "alert_smoke"))
            is_severe = True
        if "freezing" in all_conds_str or "ice" in all_conds_str:
            alert_tips.append(get_text(LANGUAGE, "alert_freezing_rain"))
            is_severe = True
        if "storm" in all_conds_str or "thunder" in all_conds_str or "torrential" in all_conds_str:
            alert_tips.append(get_text(LANGUAGE, "alert_storm"))
            is_severe = True
        if "blizzard" in all_conds_str or "heavy snow" in all_conds_str:
            alert_tips.append(get_text(LANGUAGE, "alert_blizzard"))
            is_severe = True

        # Intelligent tips
        tips = []
        is_caution = False
        if chance_of_precip > 50 or precip > 2.0:
            is_caution = True
            if int(max_precip_hour.get('chanceofsnow', 0)) > 50:
                tips.append(get_text(LANGUAGE, "snow_tip"))
            else:
                tips.append(get_text(LANGUAGE, "rain_tip"))
        
        if int(today['maxtempC']) >= 30 or feels_like >= 35:
            is_caution = True
            tips.append(get_text(LANGUAGE, "hot_tip"))
        if uv_index > 5:
            is_caution = True
            tips.append(get_text(LANGUAGE, "uv_tip"))
        if int(today['mintempC']) < 5 or (int(today['maxtempC']) - int(today['mintempC']) > 15):
            is_caution = True
            tips.append(get_text(LANGUAGE, "cold_tip"))
            
        all_tips = alert_tips + tips
        tip_text = "\n".join(all_tips) if all_tips else get_text(LANGUAGE, "nice_tip")

        # Determine color
        COLOR_SEVERE = 0xE74C3C # Red
        COLOR_CAUTION = 0xF1C40F # Yellow
        COLOR_NICE = 0x2ECC71 # Green
        COLOR_RAIN = 0x3498DB # Blue
        COLOR_SNOW = 0xECF0F1 # White
        COLOR_CLOUDY = 0x95A5A6 # Gray

        if is_severe:
            color = COLOR_SEVERE
        elif is_caution:
            if chance_of_precip > 50 or precip > 1.0:
                if "snow" in conditions_en.lower() or int(max_precip_hour.get('chanceofsnow', 0)) > 50:
                    color = COLOR_SNOW
                else:
                    color = COLOR_RAIN
            else:
                color = COLOR_CAUTION # Heat, cold, high UV
        elif "cloud" in conditions_en.lower() or "overcast" in conditions_en.lower():
            color = COLOR_CLOUDY
        else:
            color = COLOR_NICE

        embed = {
            "title": get_text(LANGUAGE, "weather_today", city=city),
            "color": color,
            "fields": [
                {
                    "name": get_text(LANGUAGE, "temp_feels_like"), 
                    "value": get_text(LANGUAGE, "temp_value", min=today['mintempC'], max=today['maxtempC'], feels=feels_like), 
                    "inline": True
                },
                {
                    "name": get_text(LANGUAGE, "conditions"), 
                    "value": get_text(LANGUAGE, "conditions_value", cond=conditions_display, uv=uv_index), 
                    "inline": True
                },
                {
                    "name": get_text(LANGUAGE, "precip_chance"), 
                    "value": get_text(LANGUAGE, "precip_value", chance=chance_of_precip, precip=precip), 
                    "inline": True
                },
                {
                    "name": get_text(LANGUAGE, "tomorrow_forecast"), 
                    "value": get_text(LANGUAGE, "tomorrow_value", cond=tomorrow_cond_display, min=tomorrow_min, max=tomorrow_max), 
                    "inline": False
                },
                {
                    "name": get_text(LANGUAGE, "tips"), 
                    "value": tip_text, 
                    "inline": False
                }
            ]
        }
        return embed
    except Exception as e:
        return {
            "title": get_text(LANGUAGE, "failed_title", city=city),
            "description": str(e),
            "color": 0xE74C3C
        }

def push_to_discord(embeds):
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print(get_text(LANGUAGE, "env_error"))
        return

    data = {
        "content": get_text(LANGUAGE, "morning_greet"),
        "embeds": embeds
    }
    
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print(get_text(LANGUAGE, "push_success"))
    else:
        print(get_text(LANGUAGE, "push_failed", code=response.status_code))

if __name__ == "__main__":
    # Read cities from environment variables, defaulting to Ottawa,Sudbury
    cities_env = os.environ.get("CITIES", "Ottawa,Sudbury")
    cities = [c.strip() for c in cities_env.split(",") if c.strip()]
    
    embeds = []
    for city in cities:
        embeds.append(get_weather_data(city))
        
    if embeds:
        push_to_discord(embeds)