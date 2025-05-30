import pandas as pd
from src.data_stats import compute_headline_lengths, headline_word_counts
from src.publisher_analysis import count_publishers, extract_top_keywords
from src.time_analysis import enrich_time_features, get_daily_article_counts, get_hourly_distribution

def main():
    df = pd.read_csv("data/raw/news_data.csv")
    
    print("\n📊 Headline Length Stats:")
    print(compute_headline_lengths(df))

    print("\n📊 Word Count Stats:")
    print(headline_word_counts(df))

    print("\n📰 Top Publishers:")
    print(count_publishers(df))

    print("\n🗝️ Top Keywords:")
    print(extract_top_keywords(df))

    df = enrich_time_features(df)

    print("\n🕒 Daily Article Counts:")
    print(get_daily_article_counts(df).head())

    print("\n🕓 Hourly Distribution:")
    print(get_hourly_distribution(df).head())

if __name__ == "__main__":
    main()
