"""
QUESTION:
Implement a function `get_most_frequent_words` that takes a text string, a list of stopwords, a minimum word length, and an integer N as input. The function should return the top N most frequent words in the text, excluding stopwords and words shorter than the minimum word length. The function should be able to handle texts containing special characters, punctuation, and multiple languages, and should use no more than 1GB of memory.
"""

import re
from collections import Counter

def get_most_frequent_words(text, stopwords, min_word_length, top_n):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    words = [word for word in words if word not in stopwords and len(word) >= min_word_length]
    word_counts = Counter(words)
    top_words = word_counts.most_common(top_n)
    return top_words