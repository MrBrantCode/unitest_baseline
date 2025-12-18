"""
QUESTION:
Create a function `word_frequency` that takes a string as input and returns a dictionary containing the frequency of each word in the string. The function should handle both uppercase and lowercase characters as separate entities, but count them as the same word. It should ignore any special characters or punctuation marks in the input string.
"""

import re
from collections import Counter

def word_frequency(string):
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    words = cleaned_string.lower().split()
    word_count = Counter(words)
    return dict(word_count)