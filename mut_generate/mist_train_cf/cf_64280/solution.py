"""
QUESTION:
Create a function named `count_words` that takes a sentence as input and returns a dictionary where the keys are distinct words from the sentence and the values are their corresponding frequencies. The function should ignore punctuation marks, special characters, and be case-insensitive.
"""

import re
from collections import Counter

def count_words(sentence):
    # Ignore special characters and punctuation, and make it lowercase
    words = re.findall(r'\b\w+\b', sentence.lower())
    # Count the frequency of each word
    result = Counter(words)
    # Return the result dictionary
    return dict(result)