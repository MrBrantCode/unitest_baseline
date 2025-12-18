"""
QUESTION:
Implement a function `cycpattern_check(a, b)` that checks if any rotation of string `b` (ignoring case and non-alphanumeric characters) is a subsequence of string `a` (ignoring case and non-alphanumeric characters), and also if both strings contain the same set of unique alphanumeric characters. Return `True` if the conditions are met, `False` otherwise.
"""

import re

def cycpattern_check(a, b):
    a = re.sub('[\W_]+', '', a).lower()
    b = re.sub('[\W_]+', '', b).lower()

    if set(a) != set(b):
        return False
    
    rotated_b = [b[i:] + b[:i] for i in range(len(b))]

    for i in range(len(a) - len(b) + 1):
        if a[i: i + len(b)] in rotated_b:
            return True
    
    return False