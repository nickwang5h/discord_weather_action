# Discord Daily Weather Bot - Architecture

## Overview
A lightweight Python script designed to fetch weather data for specified cities from `wttr.in` and push daily weather forecasts as rich embed messages to a Discord channel via Webhooks. The project is primarily designed to run automatically using GitHub Actions.

## Components
### 1. `main.py`
The core application entry point.
- **Weather Fetching**: Connects to `wttr.in` to retrieve current and forecast weather data in JSON format.
- **Data Parsing & Logic**: Calculates precipitation chance, extracts feels-like temperatures, UV index, and generates intelligent tips based on weather conditions (e.g., reminding users about rain, snow, UV, or temperature drops). It also parses hourly conditions to detect severe weather alerts (e.g., smoke, freezing rain, storm, blizzard).
- **Discord Integration**: Formats the extracted data into Discord rich embeds, dynamically selecting embed colors based on weather severity and conditions (Red for severe, Yellow for caution, Green for nice, etc.), and pushes the payload to the configured Discord Webhook URL.

### 2. `lang.py`
Internationalization (i18n) module.
- Manages text strings for the application in different languages (currently supporting English `en` and Chinese `zh`).
- Exposes a `get_text` function to retrieve formatted strings based on the configured environment language.

### 3. `.github/workflows/daily_weather.yml`
GitHub Actions workflow configuration.
- Schedules the script to run daily at a specified time (UTC 11:00).
- Sets up the Python environment, installs dependencies, and passes required GitHub Secrets (Discord Webhook URL) and environment variables (Target Cities) to `main.py`.

## Data Flow
1. **Trigger**: GitHub Actions (or local execution) triggers `main.py`.
2. **Configuration**: `main.py` reads `DISCORD_WEBHOOK_URL`, `CITIES`, and `LANGUAGE` environment variables.
3. **Data Fetching**: For each city, `main.py` sends a request to `wttr.in/<city>?format=j1`.
4. **Data Reception**: `wttr.in` returns weather data in JSON format.
5. **Processing**: `main.py` processes the JSON, utilizes `lang.py` for localized text, and constructs Discord embed objects.
6. **Push**: `main.py` sends an HTTP POST request with the constructed embeds to the `DISCORD_WEBHOOK_URL`.
7. **Delivery**: Discord receives the webhook payload and displays the weather bot message in the target channel.

## External Dependencies
- `requests`: Used for making HTTP calls to `wttr.in` and the Discord Webhook API.
- `wttr.in`: External API used for fetching weather data.
