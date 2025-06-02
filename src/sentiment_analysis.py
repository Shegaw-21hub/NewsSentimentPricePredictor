from textblob import TextBlob
import numpy as np

def calculate_sentiment(headline):
    """Quantify sentiment using TextBlob"""
    analysis = TextBlob(headline)
    return analysis.sentiment.polarity  # Range: -1 (negative) to +1 (positive)

def analyze_news_sentiment(df):
    """Batch process headlines"""
    df['sentiment'] = df['headline'].apply(calculate_sentiment)
    
    # Categorize sentiment
    df['sentiment_label'] = np.select(
        [
            df['sentiment'] > 0.1,
            df['sentiment'] < -0.1
        ],
        ['positive', 'negative'],
        default='neutral'
    )
    return df