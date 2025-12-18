"""
QUESTION:
Create a function `categorize_string(s)` that takes a string `s` as input and returns a dictionary where the keys are the distinct English alphabet characters present in `s` and the values are the corresponding counts. The function should be case-insensitive and ignore non-alphabet characters.
"""

import collections

def categorize_string(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    characters = collections.defaultdict(int)
    for char in s:
        if char in alphabet:
            characters[char] += 1
    return dict(characters)