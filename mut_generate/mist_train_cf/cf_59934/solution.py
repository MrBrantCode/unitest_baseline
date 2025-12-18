"""
QUESTION:
Design a function named `cycpattern_check` that takes two string arguments `a` and `b`. The function should determine whether `b` or any of its rotational modifications exist as uninterrupted subsequences in `a`, ignoring letter cases and special characters. The function should return a boolean value indicating whether such a subsequence exists.
"""

def cycpattern_check(a, b):
    # Remove special characters and make everything lowercase
    a = ''.join(c for c in a if c.isalnum()).lower()
    b = ''.join(c for c in b if c.isalnum()).lower()

    # Check if b is a substring of a concatenated with itself
    return b in a + a