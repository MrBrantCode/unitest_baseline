"""
QUESTION:
Create a function `word_frequency` that takes a list of strings as input, ignores case sensitivity, considers only alphanumeric characters when identifying words, and excludes common English stop words. The function should return a dictionary where the keys are unique words and the values are the frequency of each word in the input list.
"""

import re
from collections import Counter

def word_frequency(input_list):
    stop_words = set(["the", "and", "in", "of", "a", "an", "is", "are", "to", "for", "on", "at", "by", "with", "from"])
    word_count = Counter()
    
    for sentence in input_list:
        words = re.findall(r'\b\w+\b', sentence.lower())
        filtered_words = [word for word in words if word not in stop_words]
        word_count.update(filtered_words)
    
    return dict(word_count)