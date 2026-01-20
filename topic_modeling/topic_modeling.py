import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Load cleaned text
df = pd.read_csv("data/processed/cleaned_text.csv")

texts = df["clean_text"].dropna()

# Convert text to document-term matrix
vectorizer = CountVectorizer(
    max_df=0.95,
    min_df=2,
    stop_words="english"
)

dtm = vectorizer.fit_transform(texts)

# LDA Topic Model
lda = LatentDirichletAllocation(
    n_components = 7,
    random_state=42
)

lda.fit(dtm)

# Extract keywords per topic
words = vectorizer.get_feature_names_out()

topics = []
for idx, topic in enumerate(lda.components_):
    top_words = [words[i] for i in topic.argsort()[-10:]]
    topics.append({
        "topic_id": idx,
        "keywords": ", ".join(top_words)
    })

# Save results
topic_df = pd.DataFrame(topics)
topic_df.to_csv("topic_results.csv", index=False)

print("Topic modeling completed and saved to topic_results.csv")