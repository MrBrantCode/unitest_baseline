"""
QUESTION:
Create a function named `count_word_occurrences` that takes an input string `s` as a parameter and returns a hashmap where keys are the words in the string and values are their occurrence counts. The function should be case-insensitive and ignore special characters and numbers. The words should be defined as one or more letter characters.
"""

import re
from collections import Counter

def count_word_occurrences(s):
    # Normalizing the string to lower case
    s = s.lower()
    # Using regex to find all words in the string (words are defined as 1 or more letter characters)
    words = re.findall(r'\b[a-zA-Z]+\b', s)

    # Using Counter to count occurrences of each word
    word_count = Counter(words)
    return word_count