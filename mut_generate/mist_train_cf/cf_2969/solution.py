"""
QUESTION:
Write a function `word_count` that takes a string as input and returns a dictionary where the keys are the unique words in the string and the values are their corresponding counts. The function should split the string into words using spaces as separators, remove any punctuation marks, ignore any words that are less than 4 characters long, and count the occurrences of each unique word. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(m), where m is the number of unique words in the string.
"""

import re
from collections import Counter

def word_count(string):
    # Split the string into words, considering spaces as separators
    words = string.split()

    # Remove any punctuation marks present in the string
    words = [re.sub(r'\W+', '', word) for word in words]

    # Ignore any words that are less than 4 characters long
    words = [word for word in words if len(word) >= 4]

    # Count the occurrences of each unique word in the string
    word_counts = Counter(words)

    return word_counts