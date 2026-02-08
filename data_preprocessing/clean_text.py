import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    if pd.isna(text):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = [w for w in text.split() if w not in STOPWORDS]
    return " ".join(words)

# -------- LOAD RAW DATA --------
yt = pd.read_csv("data/raw/youtube_book_comments.csv")
news = pd.read_csv("data/raw/news_articles.csv")
ecom = pd.read_csv("data/raw/ecommerce_books.csv")  # Google Books / e-commerce proxy

# -------- SELECT TEXT COLUMNS --------
yt_df = pd.DataFrame({
    "clean_text": yt["comment_text"],
    "source": "youtube"
})

news_df = pd.DataFrame({
    "clean_text": (news["description"].fillna("") + " " + news["content"].fillna("")),
    "source": "news"
})

ecom_df = pd.DataFrame({
    "clean_text": ecom["full_text"] if "full_text" in ecom.columns else (ecom["title"].fillna("") + " " + ecom["description"].fillna("")),
    "source": "ecommerce"
})

# -------- COMBINE ALL --------
combined_df = pd.concat([yt_df, news_df, ecom_df], ignore_index=True)

# -------- CLEAN --------
combined_df["clean_text"] = combined_df["clean_text"].apply(clean_text)
combined_df = combined_df[combined_df["clean_text"] != ""]

# -------- DEDUP --------
combined_df = combined_df.drop_duplicates(subset=["clean_text"])

# -------- SAVE --------
combined_df.to_csv("data/processed/cleaned_text.csv", index=False)

print(f"✅ Saved {len(combined_df)} cleaned text records (YouTube + News + E-commerce)")
