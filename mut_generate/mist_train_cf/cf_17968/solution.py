"""
QUESTION:
Write a function `get_top_k_words` that takes two parameters: a string `text` and a positive integer `k`. The function should return the top `k` most common words in the `text` excluding common stop words, ignoring punctuation, and considering words in a case-insensitive manner. If multiple words have the same frequency, they should be sorted alphabetically. The input `text` is guaranteed to be non-empty and only contain words and punctuation marks.
"""

import re
from collections import Counter

def get_top_k_words(text, k):
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Exclude common stop words
    stop_words = ['the', 'and', 'in', 'to', 'a', 'it', 'can', 'be', 'for']
    
    # Split text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(word for word in words if word not in stop_words)
    
    # Get the top k most common words
    top_k_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))[:k]
    
    # Return the words as a list
    return [word for word, count in top_k_words]