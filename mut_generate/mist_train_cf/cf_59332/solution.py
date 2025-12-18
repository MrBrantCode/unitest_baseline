"""
QUESTION:
Calculate the geometric mean of three distinct numerical values. Implement a function `geometric_mean(x, y, z)` that takes three numbers as input and returns their geometric mean, which is the cube root of their product.
"""

import math

def geometric_mean(x, y, z):
    return math.pow((x * y * z), (1.0 / 3))