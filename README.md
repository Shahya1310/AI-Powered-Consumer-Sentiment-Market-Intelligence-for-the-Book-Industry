# AI-Powered Consumer Sentiment & Market Intelligence for the Book Industry

## 📌Project Overview

This project builds an AI-driven market intelligence system that analyzes large volumes of consumer feedback related to the book market (e-commerce, social media, and news) to uncover:

🔹Customer sentiment (positive / negative / neutral)

🔹Key topics and aspects (e.g., platform experience, story quality, pricing)

🔹Emerging trends and complaints

🔹Actionable business insights via a Retrieval-Augmented Generation (RAG) system

The system is designed to act as a smart assistant for market and product teams, enabling natural language querying over real customer feedback.

## 🧩Module 1: Data Collection & Preprocessing

📊 Data Sources

🔹YouTube comments related to book reviews

🔹News articles related to books, publishing, and reading trends

🔹Publicly available e-commerce/book metadata (Google Books API as a proxy source)

🛠 Tools & Libraries

🔸Python

🔸Requests

🔸Pandas

🔸NLTK

🔸Google YouTube Data API

🔸NewsAPI

### 💠Description

This module handles raw data ingestion from multiple sources and applies text cleaning and normalization to prepare the data for downstream ML tasks.
All raw text is unified into a common schema and stored as a cleaned corpus.

📤 Output

Raw data:

🔹data/raw/youtube_book_comments.csv

🔹data/raw/news_articles.csv

🔹data/raw/ecommerce_books.csv

Processed data:

🔹data/processed/cleaned_text.csv

## 🧠Module 2: Sentiment Analysis & Topic / Aspect Extraction

📌Description

This module enriches the cleaned feedback using an LLM-based pipeline to extract:

🔹Sentiment (positive / negative / neutral)

🔹Topic (e.g., platform_experience, story_quality, genre_preference)

🔹Aspect (specific issue or praise such as “app crashes”, “weak plot”)

This transforms raw feedback into a structured market intelligence dataset suitable for retrieval and analytics.

📤 Output

Enriched dataset:

🔹sentiment_analysis/book_market_sentiment_topics.csv

  (contains: clean_text, sentiment, topic, aspect)

### 🔎Module 3: RAG Pipeline & Insights Dashboards (Milestone 3)

📌Description

This module implements a Retrieval-Augmented Generation (RAG) pipeline to enable natural language querying over the enriched feedback corpus.
A prototype insights dashboard is built to visualize sentiment and topic trends.

## 🛠Tech Stack

🔸LangChain (RAG orchestration)

🔸ChromaDB (Vector Database; Pinecone-compatible architecture)

🔸HuggingFace Sentence Transformers (Embeddings)

🔸Groq API (LLM backend – LLaMA 3.1)

🔸Streamlit (Dashboard UI prototype)

📤 Output

▫️Vector database built from enriched feedback

▫️Working RAG-based Q&A system

▫️Prototype dashboards for:

▫️Sentiment distribution

▫️Topic trends

▫️Top complaints and themes

### 📈 Project Status (Milestones)

- **✅ Milestone 1 (Weeks 1–2): Setup & Data Pipeline**  
  Built a multi-source data ingestion pipeline collecting consumer feedback from YouTube, news, and e-commerce platforms. Implemented data cleaning to remove duplicates, noise, and inconsistencies, creating a unified dataset for analysis.

- **✅ Milestone 2 (Weeks 3–4): Sentiment & Topic Models**  
  Applied LLM-based analysis to extract sentiment, topics, and aspects from 2,000+ feedback records. Transformed unstructured data into structured market intelligence insights.

- **✅ Milestone 3 (Weeks 5–6): RAG & Dashboards**  
  Developed a Retrieval-Augmented Generation (RAG) pipeline using LangChain and a vector database to enable natural language querying. Built interactive dashboards to visualize sentiment distribution, topic trends, and key user complaints.

- **✅ Milestone 4 (Weeks 7–8): Alerts & Deployment**  
  Completed end-to-end system integration and deployed the solution. Enabled real-time querying through the UI and demonstrated the system’s ability to convert scattered feedback into actionable business insights.

---

### 🚀 Future Enhancements

- 🔹 Brand-specific analysis (Amazon, Kindle, Apple Books, etc.)  
- 🔹 Real-time data ingestion and streaming pipelines  
- 🔹 Automated alerts for emerging negative trends  
- 🔹 Scalable cloud deployment (Docker, Kubernetes, Azure)  
- 🔹 Advanced RAG tuning for improved retrieval accuracy
