from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk

# Download stopwords once
nltk.download('stopwords')

def extract_top_keywords(df, column='headline', max_features=20):
    """
    Enhanced for financial context - REQUIRED for Task 1's NLP analysis
    Returns: List of (keyword, count) tuples sorted by frequency
    """
    financial_stopwords = set(stopwords.words('english')).union({
        'said', 'company', 'would', 'also', 'us', 'new', 'year'  # Financial noise words
    })
    
    vec = CountVectorizer(
        stop_words=list(financial_stopwords),
        max_features=max_features,
        ngram_range=(1, 2)  # Capture phrases like "price target"
    )
    
    X = vec.fit_transform(df[column].fillna(''))
    keywords = vec.get_feature_names_out()
    counts = X.sum(axis=0).A1  # Get raw frequencies
    
    return sorted(zip(keywords, counts), key=lambda x: x[1], reverse=True)