"""
QUESTION:
Write a function `uncommon_punct_marks(text)` that takes a string `text` as input and returns a dictionary containing uncommon punctuation marks in the string as keys and their frequencies as values. A punctuation mark is considered uncommon if it is not present in Python's `string.punctuation` list. The function should handle punctuation marks in any encoding and even when they are part of a word.
"""

import string
from collections import defaultdict

def uncommon_punct_marks(text):
    common_punct_marks = list(string.punctuation)
    uncommon_punctuations = defaultdict(int)
    
    for char in text:
        if char not in common_punct_marks and not char.isalnum() and not char.isspace():
            uncommon_punctuations[char] += 1
    return uncommon_punctuations