"""
QUESTION:
Write a function `count_distinct_words(text)` that takes a string of text as input, splits it into words using whitespace, punctuation marks, and special characters as delimiters, and returns the count of distinct words. The function should be case-insensitive, exclude common stop words ("a", "an", "the"), and have a time complexity of O(n), where n is the length of the input string.
"""

import re

def count_distinct_words(text):
    # Initialize a set to store unique words
    unique_words = set()

    # Split the input string into individual words using whitespace, punctuation marks, and special characters as delimiters
    words = re.findall(r'\w+', text.lower())

    # Remove common stop words
    stop_words = set(['a', 'an', 'the'])
    words = [word for word in words if word not in stop_words]

    # Iterate through each word and add it to the set
    for word in words:
        unique_words.add(word)

    # Return the count of unique words
    return len(unique_words)