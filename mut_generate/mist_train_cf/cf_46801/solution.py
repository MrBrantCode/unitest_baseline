"""
QUESTION:
Write a function `swap_and_check(x, y)` that takes two variables `x` and `y` as input and returns their values swapped, but only if both `x` and `y` are integers. If either `x` or `y` is not an integer, the function should return the message "Please enter valid integers." The function must not use a temporary variable or any arithmetic/bitwise operators for swapping the values.
"""

def swap_and_check(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        return "Please enter valid integers."
    x, y = y, x
    return x, y