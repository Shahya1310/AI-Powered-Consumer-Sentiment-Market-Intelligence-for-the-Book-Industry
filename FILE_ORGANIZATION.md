# 📁 Project Organization — FINAL ✅

## ✨ Cleaned and Organized!

All files are now in their proper locations with **data, scripts, and documentation clearly separated**.
This structure follows standard ML project practices and is mentor‑review ready.

---

## 📂 Clean Directory Structure

```
ai-consumer-sentiment-data-collection/
│
├── 📖 DOCUMENTATION (Root Level)
│   ├── README.md                    # Main project overview
│   ├── PROJECT_STRUCTURE.md        # Technical pipeline reference
│   ├── RESULTS_GUIDE.md            # How to view outputs
│   └── FILE_ORGANIZATION.md        # Folder structure guide (this file)
│
├── ⚙️ CONFIGURATION (Root Level)
│   ├── requirements.txt            # All dependencies
│   ├── .env                        # API keys (GROQ_API_KEY)
│   └── .env.example                # Environment template
│
├── 📊 SENTIMENT ANALYSIS
│   └── sentiment_analysis/
│       ├── sentiment_analysis.py           # LLM sentiment pipeline
│       ├── sentiment_analysis_batch.py     # Batch Groq processing
│       ├── show_results_summary.py         # Statistics summary
│       ├── test_groq_connection.py         # API connectivity test
│       └── README.md                       # Usage documentation
│
├── 📊 DATA
│   └── data/
│       ├── raw/                   # Original scraped data
│       │   ├── ecommerce_books.csv
│       │   ├── news_articles.csv
│       │   └── youtube_book_comments.csv
│       │
│       └── processed/             # Cleaned & analyzed datasets
│           ├── cleaned_text.csv
│           ├── sentiment_analysis_results.csv ⭐
│           └── topic_results.csv
│
├── 🛠 PIPELINE MODULES
│   ├── data_collection/           # Scraping & API scripts
│   ├── data_preprocessing/        # Cleaning & normalization
│   └── topic_modeling/            # LLM topic extraction scripts
│
└── 📁 .git/
```

---

## ✅ What Was Cleaned

### 🗑️ Removed Duplicates

* All sentiment scripts consolidated into `sentiment_analysis/`
* Old root‑level scripts removed
* Visualization experiments removed
* Topic outputs moved into `data/processed/`

### 📍 Root Directory Now

```
ai-consumer-sentiment-data-collection/
├── .env
├── .env.example
├── .gitignore
├── FILE_ORGANIZATION.md
├── PROJECT_STRUCTURE.md
├── README.md
├── RESULTS_GUIDE.md
└── requirements.txt
```

Only essential configuration and documentation remain at root.

---

## 📍 Where Everything Is

| Item                     | Location                                        |
| ------------------------ | ----------------------------------------------- |
| Sentiment results        | `data/processed/sentiment_analysis_results.csv` |
| Topic extraction results | `data/processed/topic_results.csv`              |
| Sentiment scripts        | `sentiment_analysis/`                           |
| Data collection scripts  | `data_collection/`                              |
| Cleaning scripts         | `data_preprocessing/`                           |
| Topic modeling scripts   | `topic_modeling/`                               |
| API keys                 | `.env` (root)                                   |

---

## 🚀 Quick Start

### ▶ View Summary

```bash
cd sentiment_analysis
python show_results_summary.py
```

### ▶ Run Sentiment Analysis

```bash
cd sentiment_analysis
python sentiment_analysis_batch.py
```

### ▶ Test Groq API

```bash
cd sentiment_analysis
python test_groq_connection.py
```

---

## 📊 Results Snapshot

```
Total Records: 344
├─ Positive: ~43%
├─ Negative: ~28%
├─ Neutral:  ~29%
└─ Avg Confidence: ~0.74
```

Topic modeling results stored separately in `topic_results.csv`.

---

## 📚 Documentation Map

| File                         | Purpose              |
| ---------------------------- | -------------------- |
| README.md                    | Project overview     |
| RESULTS_GUIDE.md             | How to view outputs  |
| PROJECT_STRUCTURE.md         | Pipeline explanation |
| FILE_ORGANIZATION.md         | Folder map           |
| sentiment_analysis/README.md | Script usage         |

---

## ✅ Status

✔ Clean folder structure
✔ LLM-based sentiment analysis implemented
✔ Batch processing enabled
✔ Topic extraction via LLM
✔ Validation and insights completed
✔ Mentor‑ready repository

---

If new datasets or domains are added later, they should be placed under:

```
data/raw/
data/processed/
```

and new analysis modules under:

```
<new_module_name>/
```

This ensures the pipeline remains scalable and easy to extend.
