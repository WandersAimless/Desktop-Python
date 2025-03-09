import requests
import webbrowser

api_key = '40e474e77dbc4511bd3543a04e4c4008'
# Specify the number of articles you want (e.g., 5 articles)
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}&pageSize=50'
response = requests.get(url)
news = response.json()

# Start HTML content
html_content = """
<html>
<head>
    <title>News Headlines</title>
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
<ul>
"""

if response.status_code == 200:
    for article in news['articles']:
        title = article['title']
        url = article['url']
        html_content += f'<li><a href="{url}" target="_blank">{title}</a></li>\n'
else:
    html_content += f"<p>Failed to fetch news. Status code: {response.status_code}</p>"

# Close the HTML structure
html_content += """
</ul>
</body>
</html>
"""

# Save the HTML content to a file
with open('news_headlines.html', 'w') as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open('news_headlines.html')

# Wait for user input before closing
input("Press Enter to exit...")
