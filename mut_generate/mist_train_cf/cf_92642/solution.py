"""
QUESTION:
Write a function `compute_equation` that calculates the solution to a quadratic equation of the form ax^2 + bx + c = 0, given the coefficients a, b, and c. The function should return the unique solution if it exists, and an error message if the equation has no real solution. Assume that the equation has at most one real solution.
"""

import math

def compute_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solution exists."
    else:
        return (-b + math.sqrt(discriminant)) / (2*a)