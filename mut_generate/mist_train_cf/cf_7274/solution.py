"""
QUESTION:
Write a function named `swapNumbers` that takes two integers `x` and `y` as input and swaps their values using only bitwise operations. The function should not use any temporary variables, arithmetic operations, or conditional statements, and should be limited to a maximum of five bitwise operations.
"""

def swapNumbers(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y