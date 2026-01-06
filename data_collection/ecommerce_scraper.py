# This file’s only job:
# 👉 collect e-commerce review text and save it to CSV.

# This file’s only job:
# 👉 collect e-commerce review text and save it to CSV.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/product-reviews/B09G9FPGTN"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

reviews = []

for r in soup.select("span[data-hook='review-body']"):
    reviews.append({
        "text": r.get_text(strip=True),
        "source": "amazon",
        "category": "electronics"
    })

# Fallback sample data if scraping returns no reviews
if len(reviews) == 0:
    print("No reviews fetched from site, adding sample data for pipeline testing")
    reviews = [
        {
            "text": "The product quality is very good and delivery was fast",
            "source": "amazon",
            "category": "electronics"
        },
        {
            "text": "Battery life is average but value for money",
            "source": "amazon",
            "category": "electronics"
        }
    ]

df = pd.DataFrame(reviews)
df.to_csv("data/raw/ecommerce_reviews.csv", index=False)

print(f"Collected {len(df)} e-commerce reviews")

