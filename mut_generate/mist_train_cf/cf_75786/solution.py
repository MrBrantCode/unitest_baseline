"""
QUESTION:
Write a function `cycled_pattern_search(a, b)` that checks if string `b` or any of its cyclical permutations exist as consecutive subsequences within string `a`. The function should ignore case and non-alphanumeric elements.
"""

import re

def cycled_pattern_search(a, b):
    a = re.sub('\W+', '', a).lower()
    b = re.sub('\W+', '', b).lower()
    b_permutations = {b[i:] + b[:i] for i in range(len(b))}
    return any(cycle in a for cycle in b_permutations)