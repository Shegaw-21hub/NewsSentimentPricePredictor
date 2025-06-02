from src.date_alignment import align_dates
from src.sentiment_analysis import analyze_news_sentiment
from src.correlation_analysis import analyze_correlation
import pandas as pd

def main():
    # Load data
    news = pd.read_csv('data/news_data.csv')
    stocks = pd.read_csv('data/stock_prices/AAPL.csv', index_col='Date')
    
    # Process pipeline
    aligned_data = align_dates(news, stocks)
    sentiment_data = analyze_news_sentiment(aligned_data)
    results = analyze_correlation(sentiment_data)
    
    print(f"Correlation: {results['correlation']:.3f}")
    print(f"P-value: {results['p_value']:.4f}")
    
    # Save results
    results['analysis_df'].to_csv('results/sentiment_correlation.csv')

if __name__ == "__main__":
    main()