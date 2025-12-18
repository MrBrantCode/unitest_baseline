"""
QUESTION:
Create a function `g(x)` that calculates the value of the trigonometric polynomial `4sin^2x + 7cosx + 1` at a given angle `x`. The function should return the numerical result when `x` is equal to `π/3`. The solution should use the math library to handle trigonometric functions.
"""

import math

def g(x):
    # trigonometric polynomial
    return 4*math.sin(x)**2 + 7*math.cos(x) + 1