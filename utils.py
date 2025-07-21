import streamlit as st
import requests
from transformers import pipeline

# ✅ Load and cache the Hugging Face model once
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_model = load_model()

# ✅ Fetch Indian news from GNews API
def fetch_news(api_key, country="in", max_articles=20):
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country={country}&max={max_articles}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

# ✅ Run sentiment analysis using the model
def analyze_sentiment(text):
    if not text or text.strip() == "":
        return 0.0, "Neutral"
    
    result = sentiment_model(text[:512])[0]  # Trim long text to 512 tokens
    label = result['label']
    score = result['score']

    # Convert to signed polarity
    polarity = score if label == "POSITIVE" else -score
    return round(polarity, 4), label.capitalize()
