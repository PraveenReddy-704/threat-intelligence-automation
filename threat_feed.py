import os
import feedparser
import google.generativeai as genai
from datetime import datetime
import time

# --- Configuration ---
RSS_FEEDS = {
    "CISA Current Activity": "https://www.cisa.gov/cybersecurity-news-advisories/all.xml",
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "Bleeping Computer": "https://www.bleepingcomputer.com/feed/"
}

# Initialize Gemini
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def fetch_feed_data(feed_name, url):
    """Fetches and parses the RSS feed."""
    print(f"[*] Fetching updates from: {feed_name}")
    try:
        feed = feedparser.parse(url)
        if not feed.entries:
            print(f"[!] No entries found for {feed_name}")
            return []
        return feed.entries[:5]  # Limit to top 5 recent items per feed
    except Exception as e:
        print(f"[!] Error fetching {feed_name}: {e}")
        return []

def analyze_threat(title, summary):
    """Uses Gemini to categorize severity and technical impact."""
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
        print(f"[!] AI Analysis failed: {e}")
        return "Analysis unavailable due to API error."

def generate_report(results):
    """Saves the analyzed data into a Markdown file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "DAILY_THREAT_REPORT.md"
    
    with open(filename, "w") as f:
        f.write(f"# Daily Automated Threat Intelligence Report\n")
        f.write(f"*Generated on: {timestamp} (UTC)*\n\n")
        
        if not results:
            f.write("No new threats detected or feeds were empty.\n")
            return

        for item in results:
            f.write(f"### [{item['source']}] {item['title']}\n")
            f.write(f"- **Link:** {item['link']}\n")
            f.write(f"- **AI Analysis:**\n> {item['analysis']}\n\n")
            f.write("---\n\n")
    
    print(f"[+] Report generated successfully: {filename}")

def main():
    all_results = []
    
    for name, url in RSS_FEEDS.items():
        entries = fetch_feed_data(name, url)
        for entry in entries:
            analysis = analyze_threat(entry.title, entry.get('summary', 'No summary provided.'))
            all_results.append({
                "source": name,
                "title": entry.title,
                "link": entry.link,
                "analysis": analysis
            })
            time.sleep(1) # Small delay to respect API rate limits

    generate_report(all_results)

if __name__ == "__main__":
    main()