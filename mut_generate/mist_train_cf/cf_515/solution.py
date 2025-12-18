"""
QUESTION:
Create a function called `word_frequency` that takes a string as input and returns a dictionary mapping each unique word to its frequency. The function should ignore case sensitivity, exclude non-alphabetic characters, and disregard stop words ("the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "from", "by"). The output dictionary should be sorted in descending order by word frequency. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re
from collections import Counter

def word_frequency(string):
    stop_words = ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "from", "by"]
    clean_string = re.sub(r'[^a-zA-Z\s]', '', string.lower())
    words = clean_string.split()
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_counts