🛡️ AI-Powered Automated Threat Intelligence Feed
An automated cybersecurity intelligence tool that aggregates live threat data, analyzes severity using Google Gemini AI, and delivers real-time alerts via Telegram.

🚀 Features
Multi-Source Aggregation: Pulls live feeds from CISA, The Hacker News, and BleepingComputer.

AI Analysis: Uses gemini-2.5-flash to categorize threats by severity (Critical/High/Medium/Low) and provides a 1-sentence technical impact.

Real-time Alerting: Sends instant notifications for High and Critical threats to a private Telegram bot.

Cloud Automation: Fully automated via GitHub Actions—runs every day at 08:00 UTC.

Persistent Reporting: Generates a daily Markdown report (DAILY_THREAT_REPORT.md) for historical tracking.

🛠️ Tech Stack
Language: Python 3.10

AI Model: Google Gemini 2.5 Flash

Automation: GitHub Actions (YAML)

API Integrations: Telegram Bot API, Feedparser (RSS)

⚙️ Configuration
The following secrets must be configured in GitHub Actions:

GEMINI_API_KEY: For AI analysis.

TELEGRAM_BOT_TOKEN: Your bot's unique identifier.

TELEGRAM_CHAT_ID: Your personal chat ID for receiving alerts.
