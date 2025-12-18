"""
QUESTION:
Create a function `log(x)` to calculate the natural logarithm (base e) of a given number `x`. The function should return `Invalid input` for `x` less than or equal to 0, and the result should have a precision of at least 10 decimal places for valid inputs.
"""

import math

def log(x):
    if x <= 0:
        return "Invalid input"
    else:
        return round(math.log(x), 10)