from sklearn.feature_extraction.text import CountVectorizer

def extract_top_keywords(df, column='headline', max_features=20):
    """
    Extract most frequent keywords from news headlines.
    Returns a list of top keywords.
    """
    vec = CountVectorizer(stop_words='english', max_features=max_features)
    X = vec.fit_transform(df[column].fillna('').str.lower())
    return vec.get_feature_names_out()
