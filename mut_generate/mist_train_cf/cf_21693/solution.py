"""
QUESTION:
Write a function `swap_values(x, y)` that swaps the values of two integers `x` and `y` without using a temporary variable and only using bitwise operators. The function should have a time complexity of O(1).
"""

def swap_values(x, y):
    # XOR the two numbers
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y