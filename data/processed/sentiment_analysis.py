import pandas as pd
import os
import requests
import json
import time
import re

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_text.csv")

# Load Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY environment variable not set")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b-versatile"

def extract_json(text):
    """Safely extract JSON from LLM output"""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group() if match else None

def get_sentiment(text):
    """Sentiment analysis using Groq API"""
    # Handle non-string inputs
    if not isinstance(text, str) or len(str(text).strip()) == 0:
        return pd.Series(["neutral", 0.5])
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""Analyze the sentiment of the given text. Return ONLY a valid JSON object with "sentiment" (positive, negative, or neutral) and "confidence" (0.0 to 1.0).

Text: {str(text)[:512]}"""

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 100
    }

    try:
        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=15
        )
        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]
        json_text = extract_json(content)

        if not json_text:
            raise ValueError("Invalid JSON response")

        result = json.loads(json_text)

        sentiment = result.get("sentiment", "neutral").lower()
        confidence = round(float(result.get("confidence", 0.5)), 4)

    except Exception as e:
        error_msg = str(e)
        if len(error_msg) > 200:
            error_msg = error_msg[:200]
        print(f"[ERROR] {error_msg}")
        sentiment = "neutral"
        confidence = 0.5

    return pd.Series([sentiment, confidence])

# Apply sentiment analysis
df[["sentiment_label", "sentiment_score"]] = df["clean_text"].apply(get_sentiment)

# Save results
output_path = "data/processed/sentiment_results.csv"
df.to_csv(output_path, index=False)

print("Groq API–based sentiment analysis completed successfully.")
print(f"Results saved to: {output_path}")
