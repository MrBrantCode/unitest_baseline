"""
QUESTION:
Write a function `is_power_of_two(n)` that takes an integer `n` as input and returns `True` if `n` is a power of two and `False` otherwise. The function should assume that the input `n` is a non-negative integer.
"""

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0