"""
QUESTION:
Write a function named `calculate_quadratic_roots` that calculates the roots of a quadratic equation given its coefficients. The function should take three parameters, `a`, `b`, and `c`, representing the coefficients of the quadratic equation `ax^2 + bx + c = 0`, and return the roots of the equation. The function should handle cases where the equation has two distinct real roots, two equal real roots, or no real roots.
"""

import math

def calculate_quadratic_roots(a, b, c):
    """
    Calculate the roots of a quadratic equation given its coefficients.

    Args:
        a (float): Coefficient of the quadratic term.
        b (float): Coefficient of the linear term.
        c (float): Constant term.

    Returns:
        tuple: The roots of the quadratic equation.
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the equation has real roots
    if discriminant < 0:
        return "The equation has no real roots."
    elif discriminant == 0:
        # The equation has two equal real roots
        root = -b / (2*a)
        return root, root
    else:
        # The equation has two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2