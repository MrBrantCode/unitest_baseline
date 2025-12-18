"""
QUESTION:
Create a function named `swap` that takes two integers `x` and `y` as input and returns the swapped values using only bitwise operations. The function should not use any temporary variables or data types other than the given integers.
"""

def swap(x, y):
    if x != y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    return x, y