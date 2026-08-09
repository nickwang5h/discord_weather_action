[English](README_EN.md) | 中文

# Discord Daily Weather Bot 🌤️

这是一个简单的 Python 脚本，每天定时从 [wttr.in](https://wttr.in) 获取指定城市的天气预报，并通过 Webhook 推送到 Discord 频道中。项目内置了 GitHub Actions 工作流配置，你可以利用 GitHub 免费提供的服务器资源实现每天自动推送，无需自己购买服务器。

## 功能特性 ✨

* 🌍 支持获取多个城市的天气预报。
* 🌡️ 提供今日气温、体感温度、天气状况、降水概率、UV 指数等详细信息。
* 🔮 提供明日天气预报概览。
* 💡 根据天气状况（降水、高温、降温等）智能提供出行提示。
* 🎨 根据天气状况动态改变 Discord Embed 的颜色（如晴天橙色、雨天蓝色、雪天白色）。
* 🚀 完全依靠 GitHub Actions 自动运行，无需额外部署。

## 开始使用 🚀

你可以直接将此仓库 Fork 到你自己的 GitHub 账号下，然后配置相应的环境变量和 Secrets 即可使用。

### 1. 准备 Discord Webhook URL

1. 在你的 Discord 服务器中，选择你想要接收天气播报的频道。
2. 点击频道名称右侧的设置图标 (Edit Channel)。
3. 在左侧菜单中选择 **Integrations**，然后点击 **Webhooks**。
4. 点击 **New Webhook**，你可以修改 Webhook 的名称（比如叫“天气助手”）和头像。
5. 点击 **Copy Webhook URL**，将这个 URL 保存下来。

### 2. Fork 本仓库

点击页面右上角的 **Fork** 按钮，将项目复制到你自己的账号下。

### 3. 配置 GitHub Secrets (必须)

为了安全起见，Discord Webhook URL 不应该直接写在代码中。我们需要将其存放在 GitHub Secrets 中：

1. 在你 Fork 后的仓库页面，点击上方的 **Settings** 选项卡。
2. 在左侧菜单栏中展开 **Secrets and variables**，然后点击 **Actions**。
3. 点击右侧的 **New repository secret** 按钮。
4. **Name** 填入：`DISCORD_WEBHOOK_URL`
5. **Secret** 填入你刚才复制的 Discord Webhook URL。
6. 点击 **Add secret**。

### 4. 配置关注的城市 (可选)

默认情况下，程序会播报 "Ottawa" 和 "Sudbury" 的天气。你可以通过修改 GitHub Actions 配置文件来更改城市。

1. 在你的仓库中打开文件 `.github/workflows/daily_weather.yml`。
2. 找到第 32 行左右的 `CITIES: "Ottawa,Sudbury"`。
3. 修改为你想要的城市名称，多个城市用逗号 `,` 分隔。支持中文拼音或英文。
4. 提交 (Commit) 修改。

### 5. 开启 GitHub Actions

因为你刚刚 Fork 了仓库，GitHub 可能会默认禁用 Actions：

1. 点击仓库上方的 **Actions** 选项卡。
2. 如果看到提示，点击 **I understand my workflows, go ahead and enable them**。
3. 现在的配置是每天 UTC 11:00 (大概是北京时间晚上19:00，美东时间早上7:00) 自动运行。
4. 你也可以在左侧点击 "Daily Weather Push to Discord"，然后点击右侧的 **Run workflow** 按钮手动触发一次，测试是否配置成功。

## 本地运行调试 💻

如果你想在本地修改代码和调试：

1. 克隆仓库到本地。
2. 同步依赖：`uv sync`（`requirements.txt` 保留供现有 CI/pip 流程使用）。
3. 设置环境变量 `DISCORD_WEBHOOK_URL` 为你的 Webhook 地址。
4. (可选) 设置环境变量 `CITIES`（例如 `export CITIES="Beijing,Shanghai"`）。
5. 运行脚本：`uv run python main.py`

## 依赖声明 📦

- [requests](https://pypi.org/project/requests/)
- API 提供者: [wttr.in](https://wttr.in) (开源项目)

## License 📄

本项目基于 MIT 协议开源。
