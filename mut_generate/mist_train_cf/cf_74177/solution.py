"""
QUESTION:
Write a function `count_words` that takes a string `text` as input and returns a dictionary where the keys are the unique words from the text that end with a consonant and the values are their corresponding frequencies. The function should be case-insensitive and use regular expressions to identify words and consonants.
"""

import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    consonant_words = [word for word in words if re.match(r'\b\w*[bcdfghjklmnpqrstvwxyz]\b', word)]
    frequency = Counter(consonant_words)
    return dict(frequency)