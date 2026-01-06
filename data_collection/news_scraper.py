# This file collects news related to e-commerce / business.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news/business"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

articles = []

for a in soup.select("a.gs-c-promo-heading"):
    articles.append({
        "text": a.get_text(strip=True),
        "source": "bbc",
        "category": "business"
    })

if len(articles) == 0:
    print("No news fetched, adding sample data")
    articles = [
        {
            "text": "Online electronics sales increase during festive season",
            "source": "news",
            "category": "ecommerce"
        },
        {
            "text": "E-commerce platforms see rise in customer complaints",
            "source": "news",
            "category": "ecommerce"
        }
    ]


df = pd.DataFrame(articles)
df.to_csv("data/raw/news_articles.csv", index=False)

print(f"Collected {len(df)} news articles")
