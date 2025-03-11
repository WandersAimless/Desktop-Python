// List of RSS feed URLs (Add or modify URLs here)

const rssUrls2 = [
 
  "https://feeds.content.dowjones.io/public/rss/mw_topstories"

     // Add more RSS feed URLs here as needed
];

// Function to fetch and display RSS headlines
async function fetchInvestmentNews() {
    const newsContainer = document.getElementById("rss-investments");
    newsContainer.innerHTML = '<p>Loading news...</p>'; // Show loading message

    try {
        let allNewsHtml = ""; // Store all feeds

        for (const url of rssUrls2) {
            const proxyUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(url)}`;
            const response = await fetch(proxyUrl);
            const data = await response.json();

	    console.log("Fetched Data:", data); // Log API response

            if (data.status !== "ok") {
                throw new Error(`Failed to fetch feed: ${url}`);
            }

            const feedTitle = data.feed.title || "Unknown Source";
            let feedHtml = `<h2>${feedTitle}</h2><ul>`;

            data.items.slice(0, 5).forEach(item => { // Limit to 5 per feed
                feedHtml += `<li><a href="${item.link}" target="_blank">${item.title}</a></li>`;
            });

            feedHtml += `</ul>`;
            allNewsHtml += feedHtml;
        }

        newsContainer.innerHTML = allNewsHtml; // Update HTML with news

    } catch (error) {
        console.error("Error fetching investment news:", error);
        newsContainer.innerHTML = `<p>Error loading news. Check console for details.</p>`;
    }
}

// Run function on page load
document.addEventListener("DOMContentLoaded", fetchInvestmentNews);

// Refresh every 10 minutes
setInterval(fetchInvestmentNews, 10 * 60 * 1000);
