# app.py
import streamlit as st
from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
from utils import fetch_news, analyze_sentiment
from datetime import datetime
import json
import os

# ✅ Set page config
st.set_page_config(page_title="📰 Live News Sentiment", layout="wide")

# ✅ Set your GNews API Key
API_KEY = "0a6071bad4307a102cecbdf2e40ecd07"

# ✅ Timestamp for last updated
last_updated = datetime.now().strftime("%A, %d %B %Y | %I:%M %p")

# ✅ Title and last updated time
st.markdown("<h1 style='text-align: center; color: #336699;'>📰 Live News Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>📅 <strong>Last Updated:</strong> <code>{last_updated}</code></p>", unsafe_allow_html=True)
st.markdown("---")

# ✅ Fetch News
articles = fetch_news(API_KEY, max_articles=15)
if not articles:
    st.warning("Failed to fetch news. Please check your API key or limit.")
    st.stop()

# ✅ Load seen URLs from JSON file
SEEN_FILE = "seen_news.json"
if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, "r") as f:
        seen_urls = json.load(f)
else:
    seen_urls = []

# ✅ Process articles into DataFrame
df = pd.DataFrame([{
    "title": article["title"],
    "url": article["url"],
    "content": article["content"],
    "source": article["source"]["name"],
    "published": article["publishedAt"]
} for article in articles])

# ✅ Run sentiment analysis
df[["sentiment_score", "sentiment_label"]] = df["content"].apply(lambda x: pd.Series(analyze_sentiment(x)))

# ✅ Build display
st.markdown("<h2 style='color: #ff6b6b;'>🚨 Latest Indian Headlines with Sentiment</h2>", unsafe_allow_html=True)

new_urls = []

for idx, row in df.iterrows():
    is_new = row["url"] not in seen_urls
    sentiment_icon = "✅" if row['sentiment_label'] == "Positive" else "❌" if row['sentiment_label'] == "Negative" else "➖"

    # Headline with optional 🔥 tag
    st.markdown(f"### {'🔥 ' if is_new else ''}{row['title']}")
    st.write(f"{sentiment_icon} Sentiment: **{row['sentiment_label']}** ({row['sentiment_score']})")
    st.write(f"📰 Source: {row['source']} | 📅 Published: {row['published']}")

    # Read More button
    if st.button("🔗 Read More", key=row["url"]):
        st.markdown(f"<a href='{row['url']}' target='_blank'>Open in new tab</a>", unsafe_allow_html=True)

    st.markdown("---")

    if is_new:
        new_urls.append(row["url"])

# ✅ Save seen URLs
seen_urls += new_urls
seen_urls = list(set(seen_urls))  # Remove duplicates
with open(SEEN_FILE, "w") as f:
    json.dump(seen_urls, f)

# ✅ Search news by keyword
st.subheader("🔍 Search Headlines")
search = st.text_input("Enter keyword:")
if search:
    df_filtered = df[df["title"].str.contains(search, case=False)]
    st.success(f"Found {len(df_filtered)} result(s)")
    st.dataframe(df_filtered[["title", "source", "published", "sentiment_score", "sentiment_label"]], use_container_width=True)

# ✅ Sentiment Distribution Chart
st.markdown("---")
st.subheader("📊 Sentiment Distribution")

sent_counts = df["sentiment_label"].value_counts()
fig, ax = plt.subplots()
colors = {"Positive": "#2ecc71", "Negative": "#e74c3c", "Neutral": "#95a5a6"}
sent_counts.plot(kind="bar", color=[colors[label] for label in sent_counts.index], ax=ax)
ax.set_ylabel("Number of Articles")
ax.set_xlabel("Sentiment")
ax.set_title("News Sentiment Breakdown", fontsize=14)
st.pyplot(fig)
