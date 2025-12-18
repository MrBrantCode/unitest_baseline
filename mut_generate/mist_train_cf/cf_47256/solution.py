"""
QUESTION:
Write a function `is_not_equal(n, m)` that takes two integers `n` and `m` as input and returns `True` if `n` is not equal to its multiple by `m`, and `False` otherwise. The function should not handle invalid inputs; instead, it is assumed that `n` and `m` are integers.
"""

# Function to check if 'n' is not equal to its multiple by 'm'
def is_not_equal(n, m):
    return n != m * n