"""
QUESTION:
Implement the function `filter_and_count_words(text)` that takes a string `text` as input and returns a list of words sorted by their frequency in ascending order. The function should exclude roman numerals, symbols, and blank spaces from the count. The comparison should be case-insensitive, treating 'word' and 'Word' as the same word.
"""

import re
from collections import Counter

def filter_and_count_words(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
    words = text.split()
    words = [word for word in words if not re.fullmatch(r'[ivxlcdm]+', word)]
    word_counts = Counter(words)
    sorted_words = sorted(word_counts, key=word_counts.get)
    return sorted_words