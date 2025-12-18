"""
QUESTION:
Write a function `calculate_roots` that takes the coefficients `a`, `b`, and `c` of a quadratic equation as input and returns the roots of the equation. The function should handle cases where the discriminant is negative by printing an error message and returning `None`.
"""

import math

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("Error: The discriminant is negative. No real roots exist.")
        return None

    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    return root1, root2