"""
QUESTION:
Implement a function `count_distinct_words(text)` that takes a string as input, and returns the count of distinct words in the string. The function should consider each word as a distinct entity, split the input string using whitespace, punctuation marks, and special characters as delimiters, implement a case-insensitive solution, and remove common stop words ("a", "an", "the"). The function should have a time complexity of O(n), where n is the length of the input string.
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