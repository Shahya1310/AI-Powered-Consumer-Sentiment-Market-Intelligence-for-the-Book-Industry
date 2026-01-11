import requests
import pandas as pd
import time

API_URL = "https://www.googleapis.com/books/v1/volumes"

QUERY = "subject:technology"
MAX_RESULTS_PER_CALL = 40
TOTAL_RESULTS_TARGET = 1000   # you can increase safely

books = []
start_index = 0

while len(books) < TOTAL_RESULTS_TARGET:
    params = {
        "q": QUERY,
        "startIndex": start_index,
        "maxResults": MAX_RESULTS_PER_CALL
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    items = data.get("items", [])
    if not items:
        break

    for item in items:
        volume = item.get("volumeInfo", {})

        books.append({
            "title": volume.get("title", ""),
            "authors": ", ".join(volume.get("authors", [])),
            "description": volume.get("description", ""),
            "average_rating": volume.get("averageRating", ""),
            "categories": ", ".join(volume.get("categories", [])),
            "published_date": volume.get("publishedDate", ""),
            "source": "google_books_api"
        })

    start_index += MAX_RESULTS_PER_CALL
    print(f"Collected {len(books)} books so far...")

    time.sleep(1)   # polite delay (important)

df = pd.DataFrame(books)
df.to_csv("data/raw/ecommerce_books.csv", index=False)

print(f"Finished collecting {len(df)} books from Google Books API")
