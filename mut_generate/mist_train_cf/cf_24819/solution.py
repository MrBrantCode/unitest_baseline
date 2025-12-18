"""
QUESTION:
Write a function `solve_quadratic_equation` that takes the coefficients of a quadratic equation in the form ax^2 + bx + c = 0 and returns the solutions. The function should be able to handle complex roots.
"""

import cmath

def solve_quadratic_equation(a, b, c):
    """
    This function solves a quadratic equation in the form ax^2 + bx + c = 0.

    Parameters:
    a (float): The coefficient of x^2.
    b (float): The coefficient of x.
    c (float): The constant term.

    Returns:
    tuple: The solutions of the quadratic equation.
    """
    
    # Calculate the determinant (b^2 - 4ac)
    determinant = b**2 - 4*a*c
    
    # Calculate the solutions
    solution1 = (-b - cmath.sqrt(determinant)) / (2 * a)
    solution2 = (-b + cmath.sqrt(determinant)) / (2 * a)
    
    return solution1, solution2