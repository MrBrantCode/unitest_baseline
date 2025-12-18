"""
QUESTION:
Develop a function named `quantify_special_chars` that takes as input a nested data structure (string, list, tuple, dictionary) containing characters from any language, including emojis and special unicode characters. The function should count the frequency of each unique special character (non-printable characters and whitespaces) and return a dictionary where the keys are the special characters and the values are their frequencies. The function should be able to handle large inputs efficiently, with optimal time and space complexity.
"""

import collections
import re

def quantify_special_chars(data):
    """Count special characters in nested data structure"""
    counter = collections.Counter()
    
    if isinstance(data, str):
        for char in data:
            # Count non-printable characters and whitespaces
            if not char.isprintable() or re.match(r'\s', char):
                counter[char] += 1
    elif isinstance(data, collections.abc.Mapping):  # dict-like
        for k, v in data.items():
            counter += quantify_special_chars(k)
            counter += quantify_special_chars(v)
    elif isinstance(data, collections.abc.Iterable):  # list-like
        for item in data:
            counter += quantify_special_chars(item)
    return counter