"""
QUESTION:
Write a function `abs_difference(a, b)` that calculates the absolute difference between two numbers `a` and `b` using basic arithmetic operations (+, -, *, /) and comparisons (<, >, ==) a maximum of three times. The function should have a time complexity of O(1) and use a constant amount of space.
"""

def abs_difference(a, b):
    # Check if a is greater than b
    if a > b:
        return a - b
    # Check if a is less than b
    elif a < b:
        return b - a
    # Both numbers are equal
    else:
        return 0