"""
QUESTION:
Construct a Python function `combinations` that takes a set of lowercase alphabet characters `char_set` and a length `k` as input, and returns all possible combinations of strings of length `k` using the characters in `char_set`. The function should return the combinations as a list of strings.
"""

import itertools

def combinations(char_set, k):
    return [''.join(p) for p in itertools.product(char_set, repeat=k)]