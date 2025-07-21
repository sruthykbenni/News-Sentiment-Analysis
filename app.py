# app.py
import streamlit as st
from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
from utils import fetch_news, analyze_sentiment

# SET YOUR GNEWS API KEY HERE
API_KEY = "0a6071bad4307a102cecbdf2e40ecd07"

st.set_page_config(page_title="Indian News Sentiment", layout="wide")
st.title("📰 Indian News Sentiment Analyzer")

# Fetch News from API
articles = fetch_news(API_KEY)
if not articles:
    st.warning("Failed to fetch news. Please check your API key or limit.")
    st.stop()

# Process into DataFrame
df = pd.DataFrame([{
    "title": article["title"],
    "content": article["content"],
    "source": article["source"]["name"],
    "published": article["publishedAt"]
} for article in articles])

# Sentiment Analysis
df[["sentiment_score", "sentiment_label"]] = df["content"].apply(lambda x: pd.Series(analyze_sentiment(x)))

# Show table
st.subheader("Top Indian News Headlines with Sentiment")
st.dataframe(df[["title", "source", "published", "sentiment_score", "sentiment_label"]], use_container_width=True)

# Search Function
search = st.text_input("Search news by keyword:")
if search:
    df_filtered = df[df["title"].str.contains(search, case=False)]
    st.dataframe(df_filtered[["title", "source", "published", "sentiment_score", "sentiment_label"]])

# Plot sentiment distribution
st.subheader("📊 Sentiment Distribution")
sent_counts = df["sentiment_label"].value_counts()
fig, ax = plt.subplots()
colors = {"Positive": "green", "Negative": "red", "Neutral": "gray"}
sent_counts.plot(kind="bar", color=[colors[label] for label in sent_counts.index], ax=ax)
ax.set_ylabel("Number of Articles")
ax.set_xlabel("Sentiment")
st.pyplot(fig)
