import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bbc.com/news'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

headline_tags = soup.select('a[href^="/news"]')

news_data = []

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

df = pd.DataFrame(news_data).drop_duplicates().reset_index(drop=True)
df.to_csv("bbc_news_headlines.csv", index=False)

print("✅ Scraping successful! Sample data:")
print(df)
