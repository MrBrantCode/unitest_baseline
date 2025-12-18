"""
QUESTION:
Write a function named `swapNumbers` that takes two integers `x` and `y` as input and swaps their values using bitwise operations. The function should use no more than three bitwise operations, no conditional statements, and no arithmetic operations.
"""

def swapNumbers(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y