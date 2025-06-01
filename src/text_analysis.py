from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def extract_top_keywords(df, column='headline', max_features=20):
    """
    Enhanced for financial context
    Returns: List of (keyword, count) tuples sorted by frequency
    """
    financial_stopwords = set(stopwords.words('english')).union({
        'said', 'company', 'would', 'also', 'us', 'new', 'year'
    })
    
    vec = CountVectorizer(
        stop_words=list(financial_stopwords),
        max_features=max_features,
        ngram_range=(1, 2)
    )
    
    X = vec.fit_transform(df[column].fillna(''))
    keywords = vec.get_feature_names_out()
    counts = X.sum(axis=0).A1
    
    return sorted(zip(keywords, counts), key=lambda x: x[1], reverse=True)