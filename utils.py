# utils.py
import requests

def fetch_news(api_key, country="in", max_articles=20):
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country={country}&max={max_articles}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

from transformers import pipeline

# Load model just once
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    if not text or text.strip() == "":
        return 0.0, "Neutral"
    
    result = sentiment_model(text[:512])[0]  # limit to 512 tokens
    label = result['label']
    score = result['score']

    # Convert to numerical polarity score
    polarity = score if label == "POSITIVE" else -score
    return round(polarity, 4), label.capitalize()
