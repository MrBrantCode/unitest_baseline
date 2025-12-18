"""
QUESTION:
Create a function called `extract_unique_words` that takes a string as input and returns a set of unique words. The function should handle punctuation and be case-insensitive, treating 'word' and 'Word' as the same word.
"""

import re

def extract_unique_words(stringValue):
    words = re.findall(r'\b\w+\b', stringValue.lower())
    return set(words)