"""
QUESTION:
Write a function `f(x)` that takes one argument `x` and returns an integer value based on the following conditions: if `x` is greater than 0, return -1; if `x` is less than 0, return 1; if `x` is equal to 0, return 2. Write test cases to validate the correctness of the function for various inputs, including positive and negative numbers, zero, large numbers, and decimal numbers.
"""

def f(x):
    if x > 0:
        return -1
    elif x < 0:
        return 1
    else:
        return 2