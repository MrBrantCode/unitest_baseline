"""
QUESTION:
Write a function `swap_values` that takes two variables `a` and `b` as input and swaps their values without using a temporary variable. The function should not use the +, -, *, or / operators to perform any mathematical operations.
"""

def swap_values(a, b):
    """Swap the values of two variables without using a temporary variable."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b