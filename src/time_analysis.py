# Time trends analysis
import pandas as pd

def enrich_time_features(df):
    """
    Enhanced time features with:
    - Timezone normalization (NY time)
    - Market session detection
    - Weekend flag
    """
    # Parse with timezone handling
    df['date'] = pd.to_datetime(df['date'], utc=True).dt.tz_convert('America/New_York')
    
    # Extract enhanced features
    df['weekday'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['is_market_hours'] = df['hour'].between(9, 16)  # NYSE hours (9am-4pm)
    df['is_weekend'] = df['weekday'].isin(['Saturday', 'Sunday'])
    
    return df

def get_daily_article_counts(df):
    """Enhanced with rolling averages"""
    daily_counts = df.set_index('date').resample('D').size()
    return daily_counts.to_frame('count').assign(
        rolling_7d=lambda x: x['count'].rolling(7).mean()
    )

def get_hourly_distribution(df):
    """Enhanced with both counts and percentages"""
    hourly_counts = df['hour'].value_counts().sort_index()
    return pd.DataFrame({
        'count': hourly_counts,
        'percentage': (hourly_counts / hourly_counts.sum() * 100).round(1)
    })
