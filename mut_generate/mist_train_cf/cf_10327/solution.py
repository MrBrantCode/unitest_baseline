"""
QUESTION:
Create a function `remainder(a, b)` that calculates the remainder when the greater of two integers `a` and `b` is divided by the smaller one. The function should take two integers as input and handle negative integers by converting them to their absolute values before performing the division operation.
"""

def remainder(a, b):
    # convert negative integers to positive
    a = abs(a)
    b = abs(b)
    
    # find the greater and smaller integers
    greater = max(a, b)
    smaller = min(a, b)
    
    # calculate the remainder
    remainder = greater % smaller
    
    return remainder