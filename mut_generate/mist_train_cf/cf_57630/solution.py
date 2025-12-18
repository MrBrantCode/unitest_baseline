"""
QUESTION:
Create a function `word_frequency` that accepts a string and returns a dictionary where each key is a distinct word from the string, ignoring case, spaces, and punctuation, and each value is the frequency of the word's appearance. The function should handle empty strings and null values gracefully.
"""

import re
from collections import defaultdict

def word_frequency(string):
    if not string:
        return {}

    count_dict = defaultdict(int)
    string = string.lower()
    words = re.findall(r'\b\w+\b', string)

    for word in words:
        count_dict[word] += 1

    return count_dict