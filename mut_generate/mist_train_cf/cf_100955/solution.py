"""
QUESTION:
Implement a function `sin_exp_product(x)` that calculates the product of the sine and exponential functions for an input value `x`, but only if `x` is within the interval [0, 5]. If `x` is outside this interval, return an error message.
"""

import math

def sin_exp_product(x):
    if x < 0 or x > 5:
        return "Input value out of range. Please use a value in [0, 5]."
    else:
        return math.sin(x) * math.exp(x)