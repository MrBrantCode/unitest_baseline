"""
QUESTION:
Write a function `g(x)` to calculate the value of the trigonometric polynomial 4sin^2x + 7cosx + 1 for a given angle x, using the math library for the trigonometric functions. Evaluate `g(x)` at x = π/3.
"""

import math

def entrance(x):
    return 4 * math.pow(math.sin(x), 2) + 7 * math.cos(x) + 1