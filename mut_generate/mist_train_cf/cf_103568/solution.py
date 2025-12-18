"""
QUESTION:
Write a function `compute_equation(a, b, c)` that takes three real number coefficients `a`, `b`, and `c` of a quadratic equation `ax^2 + bx + c = 0` and returns the unique solution for `x`. If the equation has no real solution, the function should print "No real solution exists." The function should handle cases where the equation has one unique real solution and cases where the equation has no real solution.
"""

import math

def compute_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solution exists."
    else:
        return (-b + math.sqrt(discriminant)) / (2*a)