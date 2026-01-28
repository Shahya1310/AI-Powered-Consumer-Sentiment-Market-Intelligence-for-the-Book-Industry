import os
import time
import json
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

# =========================
# Setup
# =========================

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=API_KEY)

INPUT_FILE = "data/processed/cleaned_text.csv"
OUTPUT_FILE = "sentiment_analysis/book_market_sentiment_topics.csv"

# =========================
# Load Data
# =========================

df = pd.read_csv(INPUT_FILE)

# 👉 For testing, uncomment next line
# df = df.head(150)

TOTAL = len(df)
print(f"Processing {TOTAL} comments...\n")

# =========================
# Topic Categories
# =========================

TOPIC_LIST = [
    "genre_preference",
    "author_opinion",
    "story_quality",
    "pricing",
    "delivery",
    "platform_experience",
    "general_reading"
]

# =========================
# LLM Analysis Function
# =========================

def analyze_comment(text, retries=3):
    if not isinstance(text, str) or text.strip() == "":
        return "neutral", "general_reading", "empty"

    prompt = f"""
You are a market analyst for online book platforms.

Classify the following customer feedback into:

Topic (choose ONLY one):
- genre_preference
- author_opinion
- story_quality
- pricing
- delivery
- platform_experience
- general_reading

Aspect:
Short phrase describing the exact issue or praise (max 5 words)

Sentiment:
positive, negative, or neutral

Respond ONLY in valid JSON like:
{{
  "topic": "delivery",
  "aspect": "late delivery",
  "sentiment": "negative"
}}

Customer text:
\"{text[:600]}\"
"""

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=120
            )

            content = response.choices[0].message.content.strip()

            # --- Safe JSON extraction ---
            start = content.find("{")
            end = content.rfind("}") + 1
            json_text = content[start:end]

            result = json.loads(json_text)

            sentiment = result.get("sentiment", "neutral").lower()
            topic = result.get("topic", "general_reading")
            aspect = result.get("aspect", "unknown")

            # --- Validate outputs ---
            if sentiment not in ["positive", "negative", "neutral"]:
                sentiment = "neutral"

            if topic not in TOPIC_LIST:
                topic = "general_reading"

            if not aspect or len(aspect) > 40:
                aspect = "unspecified"

            return sentiment, topic, aspect

        except Exception as e:
            print(f"Retry {attempt+1}/{retries} → {str(e)[:80]}")
            time.sleep(1.5)

    return "neutral", "general_reading", "failed"

# =========================
# Run Extraction
# =========================

sentiments, topics, aspects = [], [], []

for i, text in enumerate(df["clean_text"], start=1):
    s, t, a = analyze_comment(text)

    sentiments.append(s)
    topics.append(t)
    aspects.append(a)

    if i % 10 == 0:
        print(f"Processed {i}/{TOTAL}")

    time.sleep(0.7)  # rate limit

df["sentiment"] = sentiments
df["topic"] = topics
df["aspect"] = aspects

# =========================
# Save Results
# =========================

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("\n✅ Book Market Aspect Extraction Completed")
print("Saved to:", OUTPUT_FILE)

print("\nTopic Distribution:")
print(df["topic"].value_counts())

print("\nSentiment Distribution:")
print(df["sentiment"].value_counts())
