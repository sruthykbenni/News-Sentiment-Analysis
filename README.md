# 📰 Live Indian News Sentiment Analyzer

A real-time, interactive web application that fetches the latest Indian news using the [GNews API](https://gnews.io), analyzes the sentiment of each article using Hugging Face Transformers, and presents results with intuitive visuals and alerts.

---

## 🚀 Features

- 🔍 **Live News Fetching** from Indian sources via GNews API
- 🤖 **Transformer-based Sentiment Analysis** using Hugging Face (`distilbert-base-uncased-finetuned-sst-2-english`)
- 📊 **Sentiment Distribution Charts** using Matplotlib
- 🆕 **"New Article" Detection** with highlight tags
- 🔗 **Clickable Titles** with "Read More" buttons
- 🎯 **Keyword Search** across headlines
- 🚨 **Critical Alert Section** for Negative News
- 🧠 Built with **Streamlit**, **PySpark**, **Pandas**, and **Matplotlib**
- ☁️ Deployed on **Streamlit Cloud**

---

## 📦 Tech Stack

| Technology        | Usage                           |
|-------------------|----------------------------------|
| `Streamlit`       | Frontend + UI Framework          |
| `GNews API`       | Real-time news headlines         |
| `Transformers`    | Sentiment analysis via BERT      |
| `PySpark`         | Scalable Data Processing         |
| `Matplotlib`      | Sentiment distribution chart     |
| `Pandas`          | DataFrame manipulation           |
| `JSON`            | Store seen articles              |

---

## 📸 App Preview

> 🔗 **Live App**: https://livenews-sentiment-analysis.streamlit.app/

---

## ⚙️ How It Works

1. **Fetch News**  
   Retrieves top headlines from Indian sources using GNews API.

2. **Analyze Sentiment**  
   Each article's content is run through a Hugging Face sentiment pipeline for classification (`Positive`, `Negative`, `Neutral`).

3. **Update Display**  
   New headlines are tagged 🔥.

4. **Interaction**  
   Users can:
   - View live sentiment scores
   - Search by keyword
   - Read full articles in a new tab

---

## 🛠 Installation (Local)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/news-sentiment-analyzer.git
   cd news-sentiment-analyzer
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add GNews API Key**

   * Create a `.streamlit/secrets.toml` file:

     ```toml
     API_KEY = "your_gnews_api_key"
     ```

4. **Run the App**

   ```bash
   streamlit run app.py
   ```

---

## 🧪 Folder Structure

```
news-sentiment-analyzer/
│
├── app.py                   # Main Streamlit app
├── utils.py                 # News fetch + sentiment functions
├── seen_news.json           # Stores previously seen URLs
├── requirements.txt         # Dependencies
├── README.md                # This file
└── .streamlit/
    └── secrets.toml         # API Key for GNews
```

---

## 📊 Sample Output

| Title                            | Source    | Sentiment | Score |
| -------------------------------- | --------- | --------- | ----- |
| RBI hikes repo rate again        | TOI       | Positive  | 0.84  |
| Train derailment in Odisha       | Hindustan | Negative  | -0.91 |
| Monsoon expected to arrive early | NDTV      | Neutral   | 0.01  |

---

## 🔐 API Key Setup

Register at [https://gnews.io](https://gnews.io) for a free API key and add it like so:

```toml
# .streamlit/secrets.toml
API_KEY = "your_gnews_api_key_here"
```

---

## 📈 Future Enhancements

* 📅 Sentiment trend analysis over time
* 📂 News archiving and export to CSV
* 🌐 Multilingual sentiment support (Hindi, Tamil, etc.)
* 🧠 Emotion classification (e.g., anger, fear, joy)

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improving this project — feel free to fork, raise an issue, or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for more details.

