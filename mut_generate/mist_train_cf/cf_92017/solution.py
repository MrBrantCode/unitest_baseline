"""
QUESTION:
Implement a function named `solve_quadratic_equation` that takes three coefficients (a, b, and c) of a quadratic equation ax^2 + bx + c = 0 as input and returns the roots of the equation. The function should use the quadratic formula and handle cases where the equation has two real roots, one real root, or no real roots.
"""

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots exist."