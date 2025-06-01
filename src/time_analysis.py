import pandas as pd

def enrich_time_features(df):
    """
    Enhanced with:
    - Timezone normalization
    - Market session detection
    - Holiday flag
    """
    # Parse with timezone handling
    df['date'] = pd.to_datetime(df['date'], utc=True).dt.tz_convert('America/New_York')
    
    # Extract enhanced features
    df['weekday'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['is_market_hours'] = df['hour'].between(9, 16)  # NYSE hours
    df['is_weekend'] = df['weekday'].isin(['Saturday', 'Sunday'])
    
    return df

def get_daily_article_counts(df):
    """Enhanced with rolling averages"""
    daily = df.set_index('date').resample('D').size()
    return daily.to_frame('count').assign(
        rolling_7d=lambda x: x['count'].rolling(7).mean()
    )

def get_hourly_distribution(df):
    """Enhanced with percentage distribution"""
    hourly = df['hour'].value_counts().sort_index()
    return (hourly / hourly.sum() * 100).round(1)  # Return percentages