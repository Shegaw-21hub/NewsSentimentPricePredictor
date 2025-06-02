import pandas as pd
from scipy.stats import pearsonr

def calculate_daily_returns(stock_prices):
    """Compute percentage daily returns"""
    return stock_prices['Close'].pct_change() * 100

def analyze_correlation(merged_data):
    """Calculate sentiment-return correlation"""
    # Aggregate sentiment by day
    daily_sentiment = merged_data.groupby('date')['sentiment'].mean()
    
    # Merge with returns
    analysis_df = pd.DataFrame({
        'sentiment': daily_sentiment,
        'returns': calculate_daily_returns(merged_data)
    }).dropna()
    
    # Calculate Pearson correlation
    corr, p_value = pearsonr(analysis_df['sentiment'], analysis_df['returns'])
    
    return {
        'correlation': corr,
        'p_value': p_value,
        'analysis_df': analysis_df
    }