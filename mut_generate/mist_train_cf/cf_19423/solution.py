"""
QUESTION:
Implement a function named `solve_quadratic_equation` that takes in the coefficients `a`, `b`, and `c` of a quadratic equation `ax^2 + bx + c = 0` as input and returns the solutions, discriminant value, and nature of the roots. The function should handle cases where the discriminant is greater than, equal to, or less than zero, resulting in two distinct real roots, one real root, or no real roots, respectively.
"""

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        nature = "Two distinct real roots"
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2, discriminant, nature
    elif discriminant == 0:
        nature = "One real root (a perfect square)"
        x = -b / (2*a)
        return x, discriminant, nature
    else:
        nature = "No real roots (two complex roots)"
        return None, None, discriminant, nature