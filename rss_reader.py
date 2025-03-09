import feedparser

# Replace with any RSS feed URL
rss_url = "http://feeds.bbci.co.uk/news/rss.xml"  # Example: BBC News

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Print the latest headlines
print(f"News Source: {feed.feed.title}\n")

for i, entry in enumerate(feed.entries[:10], start=1):  # Get top 10 headlines
    print(f"{i}. {entry.title}")
    print(f"   Link: {entry.link}\n")