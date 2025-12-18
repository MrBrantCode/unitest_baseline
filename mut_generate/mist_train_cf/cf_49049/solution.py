"""
QUESTION:
Write a function `is_power_of_two(n)` that checks whether a given integer `n` is a power of 2. The function should handle both positive and negative integers and return a boolean value. The integer `n` can be any 32-bit signed integer, and the function should be optimized for time complexity.
"""

def is_power_of_two(n):
    return n != 0 and ((abs(n) & (abs(n) - 1)) == 0)