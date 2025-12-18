"""
QUESTION:
Create a function `swap_values(x, y)` that takes two integers `x` and `y` as input and returns their swapped values without using a temporary variable, achieving a time complexity of O(1) using only bitwise operators.
"""

def swap_values(x, y):
    # XOR the two numbers
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y