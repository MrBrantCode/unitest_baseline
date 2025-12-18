"""
QUESTION:
Implement the function `count_words` that takes a string as input and returns a list of tuples. Each tuple contains a word and its frequency in the string. The list is sorted in descending order based on the frequency of the words and in case of a tie, the words are sorted lexicographically. The function should ignore any words that are less than 3 characters long or that contain any non-alphabetical characters and handle cases in a case-insensitive manner.
"""

import re
from collections import defaultdict

def count_words(text):
    # Preprocessing: convert to lowercase and remove non-alphabetical characters
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # Count word frequencies using defaultdict
    word_counts = defaultdict(int)
    for word in text.split():
        # Ignore words with less than 3 characters
        if len(word) >= 3:
            word_counts[word] += 1

    # Sort words by frequency (in descending order) and lexicographically
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words