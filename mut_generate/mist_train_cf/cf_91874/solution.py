"""
QUESTION:
Implement a function `find_most_frequent_words(paragraph)` that takes a string `paragraph` of up to 10^6 characters as input and returns the two most frequent words in lexicographically ascending order, ignoring case and non-alphabetic characters. If multiple words have the same frequency, return them in lexicographically ascending order.
"""

import re
from collections import Counter

def find_most_frequent_words(paragraph):
    # Preprocess paragraph
    paragraph = re.sub('[^a-zA-Z\s]', '', paragraph.lower())

    # Split paragraph into words
    words = paragraph.split()

    # Count word frequencies
    word_counts = Counter(words)

    # Sort word frequencies in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Get the two most frequent words
    most_frequent_words = [word for word, count in sorted_word_counts[:2]]

    return most_frequent_words