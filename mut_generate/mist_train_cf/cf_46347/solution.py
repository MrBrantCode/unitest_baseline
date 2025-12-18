"""
QUESTION:
Implement a function named `cycpattern_check(a, b)` that receives two string inputs `a` and `b` and determines if the second string `b`, or any version of it created by rotation, is located as a sub-sequence within the first string `a`. The function should perform the following operations: 

- disregard case sensitivity
- remove special characters
- handle character repetition within words
- locate all feasible cycles of permutation.

The function should return `True` if any cyclical permutation of `b` is a sub-sequence of `a`, and `False` otherwise.
"""

import string

def cycpattern_check(a, b):
    
    def cycle_perms(s):
        return {s[i:] + s[:i] for i in range(len(s))}
    
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation), '')
    a  = a.translate(translator).replace(" ", "").lower()
    b  = b.translate(translator).replace(" ", "").lower()
    
    for b_rot in cycle_perms(b):
        i = j = 0
        while i < len(a) and j < len(b_rot):
            if a[i] == b_rot[j]:
                j += 1
            i += 1
        if j == len(b_rot):
            return True
    return False