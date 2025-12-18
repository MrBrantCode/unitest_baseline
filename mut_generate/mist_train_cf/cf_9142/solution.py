"""
QUESTION:
Create a function `extract_unique_words(sentence)` that takes a string sentence as input and returns a tuple containing a list of unique words and a dictionary of word counts. The function should ignore case, punctuation, and common stop words. The sentence may contain uppercase and lowercase words that should be considered the same, and punctuation marks that should be excluded.
"""

import re
from collections import Counter

def extract_unique_words(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^\w\s]', '', sentence)
    words = sentence.split()
    stop_words = ["the", "and", "a", "an", "in", "on", "is", "are", "was", "were", "it", "of", "to"]
    word_counts = Counter(word for word in words if word not in stop_words)
    unique_words = list(word_counts.keys())
    return unique_words, word_counts