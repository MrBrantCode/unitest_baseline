"""
QUESTION:
Write a Python function `frustum_volume(a, b, h)` that calculates the volume of a truncated pyramidal frustum given the side length `a` of the larger base, the side length `b` of the smaller base, and the height `h`. The function should return the volume in cubic units.
"""

import math

def frustum_volume(a, b, h):
    A1 = a ** 2
    A2 = b ** 2
    return (h/3) * (A1 + math.sqrt(A1 * A2) + A2)