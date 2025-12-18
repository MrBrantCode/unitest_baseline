"""
QUESTION:
Write a function named `extract_unique_words` that takes a string `sentence` as input. The function should return two outputs: a list of unique words (case-insensitive and excluding punctuation marks and common stop words) and a dictionary or counter object containing the frequency of each unique word. The common stop words to be excluded are "the", "and", "a", "an", "in", "on", "is", "are", "was", "were", "it", "of", "to".
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