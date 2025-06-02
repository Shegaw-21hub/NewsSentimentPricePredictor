import pandas as pd

def align_dates(news_df, stock_df):
    """Align news dates with trading days"""
    # Convert to datetime and normalize
    news_df['date'] = pd.to_datetime(news_df['date']).dt.normalize()
    stock_df.index = pd.to_datetime(stock_df.index).normalize()
    
    # Merge on date
    merged = pd.merge(
        news_df,
        stock_df[['Close']],
        left_on='date',
        right_index=True,
        how='inner'
    )
    return merged