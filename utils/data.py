import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_book_data():
    """
    Load dataset + auto-generate missing business columns
    so dashboards never crash.
    """

    path = ROOT / "data" / "processed" / "book_feedback.csv"

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    # -------------------------
    # Fix sentiment safely
    # -------------------------
    if "sentiment" not in df.columns:
        df["sentiment"] = "neutral"

    df["sentiment"] = (
        df["sentiment"]
        .fillna("neutral")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # strict normalization
    df["sentiment"] = df["sentiment"].map({
        "positive": "Positive",
        "negative": "Negative",
        "neutral": "Neutral"
    })

    # anything unknown becomes Neutral
    df["sentiment"] = df["sentiment"].fillna("Neutral")

    # -------------------------
    # Confidence
    # -------------------------
    if "confidence" not in df.columns:
        df["confidence"] = 0.0

    df["confidence"] = pd.to_numeric(
        df["confidence"],
        errors="coerce"
    ).fillna(0)

    # -------------------------
    # Text column
    # -------------------------
    if "clean_text" not in df.columns:
        df["clean_text"] = ""

    # -------------------------
    # Simulated business fields
    # -------------------------

    n = len(df)

    np.random.seed(42)

    if "sales" not in df.columns:
        df["sales"] = np.random.randint(200, 5000, n)

    if "region" not in df.columns:
        df["region"] = np.random.choice(
            ["North", "South", "East", "West"], n
        )

    if "store" not in df.columns:
        df["store"] = np.random.choice(
            ["Whitefield", "Indiranagar", "BTM", "Electronic City"], n
        )

    if "category" not in df.columns:
        df["category"] = np.random.choice(
            ["Self-help", "Fiction", "Mythology", "Romance", "Sci-fi"], n
        )

    if "date" not in df.columns:
        df["date"] = pd.to_datetime("today") - pd.to_timedelta(
            np.random.randint(0, 90, n), unit="D"
        )

    return df


# backwards compatibility
load_sentiment_data = load_book_data
