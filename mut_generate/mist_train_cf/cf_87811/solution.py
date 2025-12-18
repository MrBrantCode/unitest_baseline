"""
QUESTION:
Write a function `get_common_strings` that takes a list of strings as input. The function should return the top 5 most common strings that meet the following conditions: 
- the string contains at least one uppercase letter 
- the string contains at least one lowercase letter 
- the string has a length of exactly 5 characters.
"""

import re
from collections import Counter

def get_common_strings(strings):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z]{5}$')
    valid_strings = filter(pattern.match, strings)
    counter = Counter(valid_strings)
    return counter.most_common(5)