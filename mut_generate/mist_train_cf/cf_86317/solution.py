"""
QUESTION:
Implement the `count_words` function to parse a given string and return a list of tuples, each containing a word and its frequency. The function should ignore words less than 3 characters long or with non-alphabetical characters. It should handle cases in a case-insensitive manner and count words with the same letters but different cases as the same word. The list should be sorted in descending order based on frequency and lexicographically in case of a tie. The function should be optimized for memory and processing efficiency to handle extremely large input strings.
"""

import re
from collections import defaultdict

def count_words(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    word_counts = defaultdict(int)
    for word in text.split():
        if len(word) >= 3:
            word_counts[word] += 1
    return sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))