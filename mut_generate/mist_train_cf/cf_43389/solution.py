"""
QUESTION:
Write a function `cycpattern_check(a, b)` that determines if the second word `b` or its rotations are substrings in the first word `a`. If not, the function should also check if `b` can become a substring of `a` after a series of letter swaps with adjacent letters. The function should return `True` if either condition is met and `False` otherwise.
"""

def cycpattern_check(a, b):
    # check if b is a rotation of a
    for i in range(len(b)):
        if b in a*2:
            return True
        b = b[-1] + b[:-1]
    
    # check if b can become a substring of a
    freq_a = {i: a.count(i) for i in set(b)}
    freq_b = {i: b.count(i) for i in set(b)}
    
    if not all(i in freq_a for i in freq_b): return False
    return all(freq_a[i] >= freq_b[i] for i in freq_b)