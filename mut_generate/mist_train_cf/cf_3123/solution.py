"""
QUESTION:
Write a function `get_common_strings(strings)` that takes a list of strings as input and returns the top 5 most common strings that contain at least one uppercase letter and one lowercase letter, and have a length of exactly 5 characters. The function should return a list of tuples, where each tuple contains a string and its frequency in descending order of frequency.
"""

import re
from collections import Counter

def get_common_strings(strings):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z]{5}$')
    valid_strings = filter(pattern.match, strings)
    counter = Counter(valid_strings)
    return counter.most_common(5)