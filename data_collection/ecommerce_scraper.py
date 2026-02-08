import requests
import pandas as pd
import time

API_URL = "https://www.googleapis.com/books/v1/volumes"

QUERY = "books subject:technology OR programming OR software OR AI OR data science"
MAX_RESULTS_PER_CALL = 40
TOTAL_RESULTS_TARGET = 150   # target 100–150 rows
MAX_RETRIES = 3              # don't wait forever on 429

books = []
start_index = 0
seen_ids = set()

print("📚 Starting Google Books collection (fast mode)...")

retries = 0

while len(books) < TOTAL_RESULTS_TARGET:
    params = {
        "q": QUERY,
        "startIndex": start_index,
        "maxResults": MAX_RESULTS_PER_CALL,
        "printType": "books",
        "langRestrict": "en"
    }

    response = requests.get(API_URL, params=params, timeout=20)

    if response.status_code == 429:
        retries += 1
        print(f"⚠️ Rate limited (429). Retry {retries}/{MAX_RETRIES}.")
        if retries >= MAX_RETRIES:
            print("⛔ Too many rate limits. Stopping early to avoid waiting.")
            break
        time.sleep(3)  # small pause only
        continue

    if response.status_code != 200:
        print(f"❌ HTTP Error {response.status_code}. Stopping.")
        break

    retries = 0  # reset on success

    data = response.json()
    items = data.get("items", [])
    if not items:
        print("⚠️ No more items returned by API.")
        break

    for item in items:
        volume = item.get("volumeInfo", {})
        book_id = item.get("id")

        if book_id in seen_ids:
            continue
        seen_ids.add(book_id)

        title = volume.get("title", "") or ""
        description = volume.get("description", "") or ""
        full_text = f"{title}. {description}".strip()

        if not full_text:
            continue

        books.append({
            "title": title,
            "authors": ", ".join(volume.get("authors", [])),
            "description": description,
            "full_text": full_text,
            "average_rating": volume.get("averageRating", ""),
            "categories": ", ".join(volume.get("categories", [])),
            "published_date": volume.get("publishedDate", ""),
            "source": "google_books_api"
        })

        if len(books) >= TOTAL_RESULTS_TARGET:
            break

    start_index += MAX_RESULTS_PER_CALL
    print(f"📈 Collected {len(books)} books so far...")

    time.sleep(1)  # light pause, not long waits

df = pd.DataFrame(books).drop_duplicates(subset=["title", "description"])
df.to_csv("data/raw/ecommerce_books.csv", index=False)

print(f"✅ Finished collecting {len(df)} books → data/raw/ecommerce_books.csv")
