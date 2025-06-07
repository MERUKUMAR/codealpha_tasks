import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL
url = 'https://www.bbc.com/news'

# Step 2: Set headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Step 3: Send the HTTP request
response = requests.get(url, headers=headers)

# Step 4: Parse the response with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 5: Select all news headline <a> tags that link to /news
headline_tags = soup.select('a[href^="/news"]')

# Step 6: Extract title and link from each headline
news_data = []

# Clean and skip empty titles
for tag in headline_tags:
    title = tag.get_text(strip=True)
    link = tag.get('href')

    if not title or len(title) < 5:
        continue

    if link.startswith('/'):
        link = 'https://www.bbc.com' + link

    news_data.append({
        'Title': title,
        'Link': link
    })

# Step 7: Remove duplicates and save as CSV
df = pd.DataFrame(news_data).drop_duplicates().reset_index(drop=True)
df.to_csv("bbc_news_headlines.csv", index=False)

# Step 8: Print rows
print(" Scraping successful! Sample data:")
print(df)
