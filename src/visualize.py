# src/visualize.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_wordcloud(df, column='headline'):
    text = " ".join(df[column].dropna().astype(str).tolist()).lower()
    wordcloud = WordCloud(stopwords='english', background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud of Headlines")
    plt.show()
