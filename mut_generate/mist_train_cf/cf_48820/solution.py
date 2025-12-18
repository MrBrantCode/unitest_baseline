"""
QUESTION:
Write a function `find_max(a, b, c)` that takes three numeric input parameters and returns the maximum among them. The function should be able to handle any combination of integer or floating-point numbers.
"""

def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c