import os
import feedparser
import webbrowser  # Missing import
from datetime import datetime

# List of RSS feed URLs
rss_urls = [
    "https://feeds.content.dowjones.io/public/rss/mw_topstories",
    "https://feeds.content.dowjones.io/public/rss/mw_marketpulse",
    "https://seekingalpha.com/feed.xml",
    "https://www.investing.com/rss/stock.rss",
    "https://www.investing.com/rss/market_overview.rss"
]

# Keywords to filter headlines
keywords = ["economy", "stock", "ticker", "price", "short", "long", "merger", "acquisition", "sink", "fall", "investor", "investors", "up", "down", "rise", "fall", "gain", "loss", "increase", "decrease", "surge", "dip", "boost", "drop", "plunge", "slump", "rally", "soar", "crash", "skyrocket"]

# Function to filter headlines based on keywords
def filter_headlines(feed, keywords):
    return [entry for entry in feed.entries if any(keyword.lower() in entry.title.lower() for keyword in keywords)]

# Start HTML content
html_content = """
<html>
<head>
    <title>Filtered News Headlines</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { color: #2C3E50; }
        h2 { color: #2980B9; }
        ul { list-style-type: square; }
        a { text-decoration: none; color: #3498DB; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
<h1>Filtered News Headlines</h1>
"""

# Iterate over RSS feeds and add all to ONE HTML file
for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    filtered_entries = filter_headlines(feed, keywords)

    # Ensure we have a valid feed title
    feed_title = feed.feed.get("title", "Unknown Source")

    if filtered_entries:
        html_content += f"<h2>{feed_title}</h2><ul>"
        for entry in filtered_entries:
            html_content += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>'
        html_content += "</ul>"
    else:
        html_content += f"<p>No relevant headlines found from {feed_title}.</p>"

html_content += "</body></html>"

# Define a custom folder where the HTML file will be saved
save_folder = r"C:\Users\cchri\Documents\News_Headlines"  # Change this to your preferred folder

# Ensure the folder exists (create it if it doesn't)
os.makedirs(save_folder, exist_ok=True)

# Generate filename with the current date
current_date = datetime.now().strftime("%Y-%m-%d")
filename = os.path.join(save_folder, f"Filtered_News_Headlines_{current_date}.html")

# Save the HTML file as a SINGLE file
with open(filename, "w", encoding="utf-8") as file:
    file.write(html_content)

# Open the saved HTML file in the default web browser
webbrowser.open(filename)

print(f"Results saved to '{filename}' and opened in your browser.")
