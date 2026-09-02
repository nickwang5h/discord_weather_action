[中文](README.md) | English

> [!WARNING]
> **This project is Archived**
> Daily weather forecasting was migrated on 2026-09-02 to the persistent VPS-hosted [`discord-bot`](https://github.com/nickwang5h/discord-bot) service.
> **Reason for migration**: GitHub Actions free shared runners experience severe scheduling queuing delays (often delayed by 4-10 hours until late afternoon), making timely morning delivery unreliable. The new solution runs on a persistent VPS with second-level punctuality, Open-Meteo dual-channel fallback, Canadian tiered severe weather alerts, Chinese city alias resolution, and interactive slash commands.
> This repository is kept for historical reference only; automated scheduled workflows have been retired.

# Discord Daily Weather Bot 🌤️ (Archived)

This is a simple Python script that fetches the daily weather forecast for specified cities from [wttr.in](https://wttr.in) and pushes it to a Discord channel via Webhook. The project includes a built-in GitHub Actions workflow configuration, allowing you to use GitHub's free server resources for automatic daily pushes without needing to purchase your own server.

## Features ✨

* 🌍 Supports fetching weather forecasts for multiple cities.
* 🌡️ Provides detailed information including today's temperature, feels-like temperature, weather conditions, precipitation probability, and UV index.
* 🔮 Offers a brief overview of tomorrow's weather forecast.
* 💡 Provides intelligent travel tips based on weather conditions (such as precipitation, high temperatures, temperature drops, etc.).
* 🎨 Dynamically changes the Discord Embed color based on weather conditions (e.g., orange for sunny, blue for rainy, white for snowy).
* 🚀 Runs entirely on GitHub Actions automatically, requiring no additional deployment.

## Getting Started 🚀

You can directly Fork this repository to your own GitHub account, then configure the corresponding environment variables and Secrets to use it.

### 1. Prepare Discord Webhook URL

1. In your Discord server, select the channel where you want to receive weather broadcasts.
2. Click the settings icon (Edit Channel) next to the channel name.
3. Select **Integrations** in the left menu, then click **Webhooks**.
4. Click **New Webhook**, you can modify the Webhook's name (e.g., "Weather Assistant") and avatar.
5. Click **Copy Webhook URL** and save this URL.

### 2. Fork This Repository

Click the **Fork** button in the upper right corner of the page to copy the project to your own account.

### 3. Configure GitHub Secrets (Required)

For security reasons, the Discord Webhook URL should not be written directly in the code. We need to store it in GitHub Secrets:

1. On your Forked repository page, click the **Settings** tab at the top.
2. Expand **Secrets and variables** in the left menu bar, then click **Actions**.
3. Click the **New repository secret** button on the right.
4. **Name**: enter `DISCORD_WEBHOOK_URL`
5. **Secret**: enter the Discord Webhook URL you just copied.
6. Click **Add secret**.

### 4. Configure Cities to Monitor (Optional)

By default, the program broadcasts the weather for "Ottawa" and "Sudbury". You can change the cities by modifying the GitHub Actions configuration file.

1. Open the file `.github/workflows/daily_weather.yml` in your repository.
2. Find `CITIES: "Ottawa,Sudbury"` around line 32.
3. Modify it to your desired city names, separating multiple cities with a comma `,`. Pinyin or English are supported.
4. Commit the changes.

### 5. Enable GitHub Actions

Since you just Forked the repository, GitHub might disable Actions by default:

1. Click the **Actions** tab at the top of the repository.
2. If you see a prompt, click **I understand my workflows, go ahead and enable them**.
3. The current configuration is to run automatically at 11:00 UTC daily (which is roughly 19:00 Beijing Time, 7:00 EST).
4. You can also manually trigger it once by clicking "Daily Weather Push to Discord" on the left, then clicking the **Run workflow** button on the right, to test if the configuration is successful.

## Local Running & Debugging 💻

If you want to modify and debug the code locally:

1. Clone the repository to your local machine.
2. Sync dependencies with `uv sync` (`requirements.txt` remains for the existing CI/pip workflow).
3. Set the environment variable `DISCORD_WEBHOOK_URL` to your Webhook address.
4. (Optional) Set the environment variable `CITIES` (e.g., `export CITIES="Beijing,Shanghai"`).
5. Run the script: `uv run python main.py`

## Dependencies 📦

- [requests](https://pypi.org/project/requests/)
- API Provider: [wttr.in](https://wttr.in) (Open source project)

## License 📄

This project is open-sourced under the MIT License.
