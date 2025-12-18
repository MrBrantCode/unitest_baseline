"""
QUESTION:
Create a function called `word_frequency` that takes a string as input and returns a dictionary containing the frequency of each word in the string. The function should handle both uppercase and lowercase characters as separate entities and ignore any special characters or punctuation marks in the input string. However, the frequency of each word should be case-insensitive. The function should return a dictionary where the keys are the words and the values are their corresponding frequencies.
"""

import re
from collections import Counter

def word_frequency(string):
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    words = cleaned_string.lower().split()
    word_count = Counter(words)
    return dict(word_count)