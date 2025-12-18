"""
QUESTION:
Given a string `s` of length between 1 and 10^5, consisting of only lowercase English letters, write a function `firstAndLastUnique(s)` that returns a list containing the indices of the first and last non-repeating characters in `s`. If no such characters exist, return a list `[-1, -1]`.
"""

import collections

def firstAndLastUnique(s):
    count = collections.Counter(s)
    first_unique = -1
    last_unique = -1
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            if first_unique == -1: # First unique character
                first_unique = idx
            last_unique = idx # Keep updating. Will finally hold last unique character
    return [first_unique, last_unique]