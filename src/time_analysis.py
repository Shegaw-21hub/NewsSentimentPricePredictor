import pandas as pd

def enrich_time_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['weekday'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    return df

def get_daily_article_counts(df):
    return df.set_index('date').resample('D').size()

def get_hourly_distribution(df):
    return df['hour'].value_counts().sort_index()
