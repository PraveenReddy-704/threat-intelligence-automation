# 🛡️ Automated AI Threat Intelligence Feed

An automated OSINT pipeline that aggregates daily cybersecurity news and uses **Google Gemini 1.5 Flash** to provide technical impact analysis and severity scoring.

## 🚀 How It Works
1. **Fetch:** Pulls the latest advisories from CISA, The Hacker News, and Bleeping Computer via RSS.
2. **Analyze:** Sends summaries to Gemini-2.5-Flash with a custom prompt to determine severity (Critical/High/Medium/Low) and technical impact.
3. **Report:** Generates a `DAILY_THREAT_REPORT.md` file.
4. **Automate:** GitHub Actions triggers the workflow every day at 08:00 UTC.

## 🛠️ Tech Stack
- **Language:** Python 3.10
- **AI:** Google Generative AI (Gemini API)
- **Automation:** GitHub Actions
- **Libraries:** `feedparser`, `google-generativeai`

## 📊 Sample Output
Check [DAILY_THREAT_REPORT.md](./DAILY_THREAT_REPORT.md) for the latest updates.

## ⚙️ Setup (For Local Testing)
1. Clone the repo: `git clone <your-repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API key: `export GEMINI_API_KEY='your_key_here'`
4. Run the script: `python threat_feed.py`

---
*Developed for my Cybersecurity Portfolio.*
