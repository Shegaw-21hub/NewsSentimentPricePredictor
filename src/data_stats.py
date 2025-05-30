# Descriptive stats functions
def compute_headline_lengths(df):
    df['headline_length'] = df['headline'].str.len()
    return df['headline_length'].describe()

def headline_word_counts(df):

    df['word_count'] = df['headline'].str.split().apply(len)
    return df['word_count'].describe()
