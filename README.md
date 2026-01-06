# AI-Driven Consumer Sentiment & Market Trend Intelligence

## Project Overview
This project aims to analyze consumer sentiment and market trends using data collected from e-commerce platforms, social media, and news sources.

This repository will be developed incrementally as part of the internship, starting with the data collection module.

---

## Current Module: Data Collection

### Data Sources
- E-commerce product reviews (public review pages)
- News articles related to e-commerce and business categories

### Tools & Libraries Used
- Python
- Requests
- BeautifulSoup
- Pandas

### Description
The data collection module fetches raw textual data from e-commerce review pages and business news websites. The collected data is stored in structured CSV format to support downstream sentiment analysis, topic modeling, and trend detection pipelines.

Due to scraping restrictions on some websites, fallback sample data is included to ensure pipeline testing and continuity.

### Output
Raw data is stored in the following files:
- `data/raw/ecommerce_reviews.csv`
- `data/raw/news_articles.csv`

---

## Project Status
✔ Data Collection module completed  
⬜ Data Preprocessing  
⬜ Sentiment & Topic Analysis  
⬜ RAG Pipeline  
⬜ Chatbot, Dashboards & Alerts
