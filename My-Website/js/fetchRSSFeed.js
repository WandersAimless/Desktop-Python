// List of RSS feed URLs (Add or modify URLs here)
const rssUrls = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", // New York Times
    // Add more RSS feed URLs here as needed
];

// Function to fetch and display RSS headlines
async function fetchRSSFeed() {
    const feedContainer = document.getElementById("rss-headlines");
    feedContainer.innerHTML = "<p>Loading news...</p>"; // Show loading message

    try {
        let allNewsHtml = ""; // Store all feeds

        for (const url of rssUrls) {
            const proxyUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(url)}`;
            const response = await fetch(proxyUrl);
            const data = await response.json();

            if (data.status !== "ok") {
                throw new Error(`Failed to fetch feed: ${url}`);
            }

            const feedTitle = data.feed.title || "Unknown Source";
            let feedHtml = `<h2>${feedTitle}</h2><ul>`;

            // Limit to 5 articles per feed
            data.items.slice(0, 5).forEach(item => {
                feedHtml += `<li><a href="${item.link}" target="_blank">${item.title}</a></li>`;
            });

            feedHtml += "</ul>";
            allNewsHtml += feedHtml;
        }

        feedContainer.innerHTML = allNewsHtml; // Update HTML with news

    } catch (error) {
        console.error("Error fetching RSS feed:", error);
        feedContainer.innerHTML = "<p>Failed to load RSS feed.</p>";
    }
}

// Run the function on page load
document.addEventListener("DOMContentLoaded", fetchRSSFeed);

// Refresh every 10 minutes
setInterval(fetchRSSFeed, 10 * 60 * 1000);
;
