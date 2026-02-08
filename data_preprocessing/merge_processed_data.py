import pandas as pd
from pathlib import Path

# List all sentiment-annotated datasets here
sentiment_files = [
    "data/processed/cleaned_text.csv",
    # "data/processed/sentiment_analysis_results_batch.csv",  
    # "data/processed/youtube_sentiment.csv",
    # "data/processed/news_sentiment.csv",
    # "data/processed/ecommerce_sentiment.csv",

]

dfs = []

for f in sentiment_files:
    path = Path(f)
    if not path.exists():
        print(f"⚠️ Skipping missing file: {f}")
        continue

    df = pd.read_csv(f)
    print(f"Loaded {f} with {len(df)} rows")

    # Normalize column names (safety)
    df.columns = [c.strip().lower() for c in df.columns]

    # Enforce required schema
    required_cols = ["clean_text", "sentiment", "confidence"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"❌ File {f} is missing required columns: {missing}")

    # Keep only required + optional metadata
    keep_cols = ["clean_text", "sentiment", "confidence"]
    if "source" in df.columns:
        keep_cols.append("source")

    df = df[keep_cols]

    dfs.append(df)

if not dfs:
    raise RuntimeError("❌ No valid sentiment files loaded. Cannot build final dataset.")

final_df = pd.concat(dfs, ignore_index=True)

# Clean text
final_df["clean_text"] = final_df["clean_text"].astype(str).str.strip()
final_df = final_df[final_df["clean_text"] != ""]

# Drop duplicates
final_df = final_df.drop_duplicates(subset=["clean_text"])

# Optional: basic sanity filters
final_df["sentiment"] = final_df["sentiment"].astype(str).str.lower().str.strip()

# Save final dataset
output_path = "data/processed/book_feedback.csv"
final_df.to_csv(output_path, index=False)

print(f"✅ final_book_feedback.csv created with {len(final_df)} rows")
print("Columns:", list(final_df.columns))
