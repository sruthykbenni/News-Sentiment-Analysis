# utils.py
import requests
from textblob import TextBlob

def fetch_news(api_key, country="in", max_articles=20):
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country={country}&max={max_articles}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

def analyze_sentiment(text):
    if not text:
        return 0.0, "Neutral"
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    label = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    return score, label
