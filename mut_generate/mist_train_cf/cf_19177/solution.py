"""
QUESTION:
Write a function `find_median(a, b, c)` to calculate the median of three numbers `a`, `b`, and `c`. The function cannot use any conditional statements (if, elif, else) or comparison operators (>, <, ==), but can only use mathematical operations and functions.
"""

def find_median(a, b, c):
    return (a + b + c) - (max(a, b, c) + min(a, b, c))