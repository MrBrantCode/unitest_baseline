"""
QUESTION:
Write a function `cycpattern_check(a, b)` that checks whether the string `b` or its cyclic permutations are an uninterrupted subset of the string `a`, ignoring case and punctuation differences. The function should be efficient for long strings and work with language-specific symbols.
"""

import re

def cycpattern_check(a, b):
    # Remove punctuation and convert to lowercase
    a = re.sub(r'\W+', '', a).lower()
    b = re.sub(r'\W+', '', b).lower()

    # Check all cyclic permutations of b in a
    for i in range(len(b)):
        if b in a:
            return True
        else:
            # Permute b - Shift b one character to the right 
            b = b[-1] + b[:-1]
    return False