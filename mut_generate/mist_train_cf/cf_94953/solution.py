"""
QUESTION:
Create a function named `word_count` that takes a string as input, and returns a dictionary where the keys are the unique words from the string and the values are their corresponding counts. The function should be case-insensitive, ignore punctuation, and handle special characters and words with apostrophes correctly. The function should be efficient enough to handle very large input strings.
"""

import re
from collections import defaultdict

def word_count(string):
    string = re.sub(r'[^\w\s]', '', string.lower())
    words = string.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    return dict(word_counts)