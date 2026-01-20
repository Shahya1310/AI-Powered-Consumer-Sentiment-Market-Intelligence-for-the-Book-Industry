# AI-Driven Consumer Sentiment & Market Trend Intelligence

## Project Overview
This project aims to analyze consumer sentiment and market trends using data collected from e-commerce platforms, social media, and news sources.

This repository will be developed incrementally as part of the internship, starting with the data collection module.

---

## Module 1: Data Collection & Preprocessing

### Data Sources
- E-commerce product reviews (public review pages / sample datasets)
- News articles related to e-commerce and business categories

### Tools & Libraries Used
- Python
- Requests
- BeautifulSoup
- Pandas
- NLTK

### Description
The data collection module fetches raw textual data from public sources and fallback datasets where scraping restrictions apply.  
Preprocessing is applied to clean and normalize text for downstream analysis tasks.

### Output
- Raw data:
  - `data/raw/ecommerce_books.csv`
  - `data/raw/news_articles.csv`
- Processed data:
  - `data/processed/cleaned_text.csv`

---

## Current Module: Sentiment Analysis & Topic Modeling

### Description
This module focuses on extracting insights from cleaned text data using sentiment analysis and topic modeling techniques.  
Initial implementations have been completed and outputs are generated for validation and analysis.

### Output
- `data/processed/sentiment_results.csv`
- `topic_results.csv`

---

## Project Status
✔ Data Collection module completed  
✔ Data Preprocessing  
✔ Sentiment & Topic Analysis  
⬜ RAG Pipeline  
⬜ Chatbot, Dashboards & Alerts
