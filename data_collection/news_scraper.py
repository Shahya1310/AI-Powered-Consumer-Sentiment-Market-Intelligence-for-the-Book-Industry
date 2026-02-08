from datetime import datetime, timedelta
import requests
import pandas as pd
import time

API_KEY = "d851e72bb7c5472f96b610148face72a"
BASE_URL = "https://newsapi.org/v2/everything"

QUERY = "(books OR publishing OR ebook OR reading OR book sales OR author OR bookstore)"
PAGE_SIZE = 100

articles = []

# Collect articles from last 30 days in 5-day windows
end_date = datetime.utcnow()
start_date = end_date - timedelta(days=30)

current_start = start_date

while current_start < end_date:
    current_end = min(current_start + timedelta(days=5), end_date)
    page = 1

    print(f"\n📅 Fetching from {current_start.date()} to {current_end.date()}")

    while True:
        params = {
            "q": QUERY,
            "language": "en",
            "pageSize": PAGE_SIZE,
            "page": page,
            "from": current_start.strftime("%Y-%m-%d"),
            "to": current_end.strftime("%Y-%m-%d"),
            "apiKey": API_KEY,
            "sortBy": "publishedAt"
        }

        response = requests.get(BASE_URL, params=params, timeout=20)

        if response.status_code != 200:
            print(f"❌ HTTP Error {response.status_code} for {current_start.date()}–{current_end.date()}")
            break

        data = response.json()
        fetched = data.get("articles", [])
        if not fetched:
            break

        for item in fetched:
            articles.append({
                "title": item.get("title", ""),
                "description": item.get("description", ""),
                "content": item.get("content", ""),
                "source": item.get("source", {}).get("name", ""),
                "published_at": item.get("publishedAt", ""),
                "category": "ecommerce_news"
            })

        page += 1
        time.sleep(1)

    current_start = current_end

df = pd.DataFrame(articles).drop_duplicates(subset=["title", "content"])
df.to_csv("data/raw/news_articles.csv", index=False)

print(f"\n✅ Finished collecting {len(df)} news articles")