"""
QUESTION:
Write a function `are_equal(x, y)` that takes two integers as input and returns a boolean value indicating whether they are equal. The function must not use any comparison operators (==, !=, >, <).
"""

def are_equal(x, y):
    return abs(x - y) + abs(y - x) == 0