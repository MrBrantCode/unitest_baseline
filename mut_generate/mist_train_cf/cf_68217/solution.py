"""
QUESTION:
Write a function `cycpattern_check(a, b)` that checks if string `b` is a substring of string `a` or if it can be transformed into a substring of `a` by performing at most one character substitution and/or at most three cyclic rotations. If `b` can be transformed into a substring of `a`, return `True`; otherwise, return `False`.
"""

def cycpattern_check(a, b):
    b_chars = set(b)
    if all(char in a for char in b_chars):
        if b in a or b[::-1] in a:
            return True
        else:
            a_chars = set(a)
            substituted = []
            for char in b:
                if char not in a_chars:
                    substituted.append(char)
            if len(substituted) <= 1:
                for char in substituted:
                    b = b.replace(char, list(a_chars.difference(b_chars))[0], 1)
                for i, char in enumerate(b):
                    swaps = 0
                    while b not in a and b[::-1] not in a and swaps < 3:
                        b = b[i+1:] + b[:i+1]
                        swaps += 1
                    if b in a or b[::-1] in a:
                        return True
    return False