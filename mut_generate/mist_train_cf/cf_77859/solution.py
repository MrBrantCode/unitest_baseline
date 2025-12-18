"""
QUESTION:
Write a function `cycpattern_check(a, b)` that takes two strings `a` and `b` as input and returns `True` if `b` or any of its cyclic permutations are contiguous subsequences in `a`, and `False` otherwise. The function should be case-insensitive and ignore non-alphabetic characters.
"""

def cycpattern_check(a, b):
    def sanitize(text):
        return ''.join(filter(str.isalpha, text)).lower()

    a, b = sanitize(a), sanitize(b)

    for i in range(len(b)):
        if b in a or b[::-1] in a:
            return True
        b = b[-1:] + b[:-1]
    return False