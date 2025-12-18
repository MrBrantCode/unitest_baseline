"""
QUESTION:
Write a function `count_consonants(s)` that takes a string `s` as input, converts it to all uppercase characters, removes any additional spaces, special characters, and numbers, and returns a dictionary where keys are uppercase consonants and values are their respective counts in the transformed string.
"""

import re

def count_consonants(s):
    s = re.sub(r"[^a-zA-Z\s]", "", s)  # remove special characters and numbers
    s = " ".join(s.split())  # remove extra spaces
    s = s.upper()  # convert to uppercase

    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    counts = dict()

    for c in s:
        if c in consonants:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1

    return counts