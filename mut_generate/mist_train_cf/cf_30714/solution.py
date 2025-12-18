"""
QUESTION:
Implement a function `calculate_roots(a, b, c)` that calculates the roots of a quadratic equation `ax^2 + bx + c = 0`. The function should take the coefficients `a`, `b`, and `c` as input and return the two roots `x_c` and `x_d` as a tuple.
"""

import math

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = math.sqrt(discriminant)
    x_c = (-b + sqrt_discriminant) / (2*a)
    x_d = (-b - sqrt_discriminant) / (2*a)
    return x_c, x_d