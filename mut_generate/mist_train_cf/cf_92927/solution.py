"""
QUESTION:
Create a function `most_frequent_char(s)` that takes a string `s` as input and returns the most frequent alphabetic character in the string, excluding any punctuation characters and considering case insensitivity.
"""

import string
from collections import Counter

def most_frequent_char(s):
    # Remove punctuation characters from the string
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # Count the frequency of alphabetic characters
    counts = Counter(c for c in s.lower() if c.isalpha())
    
    # Find the most frequent character
    most_frequent = max(counts, key=counts.get)
    
    return most_frequent