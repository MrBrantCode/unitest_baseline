"""
QUESTION:
Develop a function `cycpattern_check(a, b)` that takes two string arguments and determines whether the secondary string `b` or any of its cyclic permutations occur as contiguous subsequences of the primary string `a`. The function should be case-insensitive and ignore non-alphanumeric characters.
"""

import re

def cycpattern_check(a, b):
    # Preprocessing of strings
    a = "".join(re.findall("[a-zA-Z0-9]*", a)).lower()
    b = "".join(re.findall("[a-zA-Z0-9]*", b)).lower()

    # Function for getting all the cyclic permutations
    cycle = lambda s: [s[i:] + s[:i] for i in range(len(s))]

    # Check for presence of b or its cyclic permutations in a
    return any(c in a for c in cycle(b))