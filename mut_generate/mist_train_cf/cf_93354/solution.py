"""
QUESTION:
Create a function named `count_words` that takes a string as input and returns the number of occurrences of each unique word in the string. The function should ignore punctuation and consider words in a case-insensitive manner.
"""

import re
from collections import Counter

def count_words(string):
    # Remove punctuation and convert string to lowercase
    cleaned_string = re.sub(r'[^\w\s]', '', string).lower()
    # Split the cleaned string into words
    words = cleaned_string.split()
    # Count the occurrences of each unique word
    word_counts = Counter(words)
    return word_counts