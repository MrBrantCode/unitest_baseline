"""
QUESTION:
Write a function named `swap_without_temp` that takes two integers `x` and `y` and swaps their values without using a temporary variable.
"""

def swap_without_temp(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y