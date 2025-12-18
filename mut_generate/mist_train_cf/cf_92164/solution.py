"""
QUESTION:
Create a function `count_words(word_string)` that takes a string of words as input and returns a dictionary with the count of each word, excluding common English stop words and ignoring case sensitivity. The function should handle punctuation marks and special characters properly, and be able to handle large input strings efficiently without causing performance issues or running out of memory.
"""

import re
from collections import Counter

def count_words(word_string):
    # Convert the string to lowercase
    word_string = word_string.lower()

    # Define the list of common English stop words
    stop_words = ["a", "an", "the", "is", "of", "but", "some", "are"]

    # Remove punctuation marks and special characters
    word_string = re.sub(r'[^\w\s]', '', word_string)

    # Split the string into individual words
    words = word_string.split()

    # Remove stop words from the list of words
    words = [word for word in words if word not in stop_words]

    # Count the occurrences of each word
    word_count = Counter(words)

    return word_count