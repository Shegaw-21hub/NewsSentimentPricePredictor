# Time trends analysis
def count_publishers(df, top_n=10):
    return df['publisher'].value_counts().head(top_n)

def extract_top_keywords(df, n=20):
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer(stop_words='english', max_features=n)
    X = vec.fit_transform(df['headline'].fillna('').str.lower())
    return vec.get_feature_names_out()
