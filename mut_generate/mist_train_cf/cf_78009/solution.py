"""
QUESTION:
Construct a function `calculate_expression(x, y, z)` that calculates the result of the trigonometric expression `2*sin(x) + 3*cos(y) - 4*tan(z^2)`, where `x`, `y`, and `z` are in radians. The function should take in three arguments `x`, `y`, and `z` and return the calculated result.
"""

import math

def calculate_expression(x, y, z):
    result = 2*math.sin(x) + 3*math.cos(y) - 4*math.tan(z**2)
    return result