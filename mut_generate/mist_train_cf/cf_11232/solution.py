"""
QUESTION:
Create a function named `square` that takes one argument `x`. The function should return the square of `x` if `x` is greater than 0, otherwise return 0. You cannot use the ternary expression or any built-in mathematical functions or operators (except for multiplication and comparison operators).
"""

def square(x):
    if x > 0:
        return x * x
    else:
        return 0