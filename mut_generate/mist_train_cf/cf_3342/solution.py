"""
QUESTION:
Implement the `get_most_frequent_words` function that takes four parameters: `text`, `stopwords`, `min_word_length`, and `top_n`. The function should return a list of the top `top_n` most frequently used words in the `text`, ignoring `stopwords` and words with less than `min_word_length` characters. The function should handle texts with special characters, punctuation, and diacritical marks, treating words with different diacritical marks as distinct words. The function should be efficient in handling large inputs of up to 100 million words and use no more than 1GB of memory.
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