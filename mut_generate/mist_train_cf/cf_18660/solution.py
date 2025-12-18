"""
QUESTION:
Develop a function named `top_k_words` that takes two parameters: a string `text` and an integer `k`, and returns the top `k` most frequently occurring words in the given `text`. The function should ignore common stop words such as "the", "a", "an", etc. and consider words in a case-insensitive manner.
"""

import re
from collections import Counter

def top_k_words(text, k):
    stop_words = {'the', 'a', 'an', 'and', 'in', 'on', 'is', 'it', 'to', 'of'}
    words = re.findall(r'\w+', text.lower())
    word_count = Counter(words)
    word_count = {word: count for word, count in word_count.items() if word not in stop_words}
    top_k = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:k]
    return top_k