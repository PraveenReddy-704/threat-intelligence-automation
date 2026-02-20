import os
import feedparser
import google.generativeai as genai
from datetime import datetime
import time
import requests  # New: Required for Telegram

# --- Configuration ---
RSS_FEEDS = {
    "CISA Current Activity": "https://www.cisa.gov/cybersecurity-news-advisories/all.xml",
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "Bleeping Computer": "https://www.bleepingcomputer.com/feed/"
}

# Secrets from Environment Variables
API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Initialize Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def send_telegram_alert(title, source, analysis, link):
    """Sends a formatted alert to Telegram."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("[!] Telegram credentials missing. Skipping alert.")
        return

    # Create the message using Markdown formatting
    message = (
        f"🚨 *HIGH SEVERITY THREAT DETECTED*\n\n"
        f"*Source:* {source}\n"
        f"*Title:* {title}\n\n"
        f"*AI Analysis:* {analysis}\n\n"
        f"[Read Full Article]({link})"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"[+] Telegram alert sent for: {title}")
        else:
            print(f"[!] Telegram API error: {response.text}")
    except Exception as e:
        print(f"[!] Telegram Alert Failed: {e}")

def fetch_feed_data(feed_name, url):
    print(f"[*] Fetching updates from: {feed_name}")
    try:
        feed = feedparser.parse(url)
        return feed.entries[:5] if feed.entries else []
    except Exception as e:
        print(f"[!] Error fetching {feed_name}: {e}")
        return []

def analyze_threat(title, summary):
    prompt = (
        f"Analyze this security news.\n"
        f"Title: {title}\n"
        f"Summary: {summary}\n\n"
        f"Categorize its severity (Critical/High/Medium/Low) and give a 1-sentence technical impact."
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Analysis unavailable."

def generate_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("DAILY_THREAT_REPORT.md", "w") as f:
        f.write(f"# Daily Automated Threat Intelligence Report\n")
        f.write(f"*Generated on: {timestamp} (UTC)*\n\n")
        for item in results:
            f.write(f"### [{item['source']}] {item['title']}\n")
            f.write(f"- **Link:** {item['link']}\n")
            f.write(f"- **AI Analysis:**\n> {item['analysis']}\n\n")
            f.write("---\n\n")

def main():
    all_results = []
    for name, url in RSS_FEEDS.items():
        entries = fetch_feed_data(name, url)
        for entry in entries:
            analysis = analyze_threat(entry.title, entry.get('summary', ''))
            
            # Store result
            item = {
                "source": name,
                "title": entry.title,
                "link": entry.link,
                "analysis": analysis
            }
            all_results.append(item)

            # ALERT LOGIC: If AI says Critical or High, send to Telegram
            if "Critical" in analysis or "High" in analysis:
                send_telegram_alert(item['title'], item['source'], item['analysis'], item['link'])
            
            time.sleep(1) # Rate limit protection

    generate_report(all_results)

if __name__ == "__main__":
    main()
    generate_report(all_results)

if __name__ == "__main__":

    main()
