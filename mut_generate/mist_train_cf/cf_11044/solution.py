"""
QUESTION:
Create a function called `word_count` that takes a string of words as input and returns a dictionary where the keys are the words and the values are their respective occurrence counts. The function should ignore punctuation and be case-insensitive.
"""

import re
from collections import Counter

def word_count(string):
    string = re.sub(r'[^\w\s]', '', string).lower()
    words = string.split()
    return dict(Counter(words))