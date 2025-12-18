"""
QUESTION:
Write a function named `solve_quadratic` that takes in three parameters, `a`, `b`, and `c`, representing the coefficients of a quadratic equation in the form ax^2 + bx + c = 0. Return the solutions to the equation.
"""

import math

def solve_quadratic(a, b, c):
    """
    Returns the solutions to the quadratic equation ax^2 + bx + c = 0.

    Args:
        a (float): The coefficient of the quadratic term.
        b (float): The coefficient of the linear term.
        c (float): The constant term.

    Returns:
        tuple: A tuple containing the two solutions to the quadratic equation.
    """

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is negative
    if discriminant < 0:
        return "No real solutions"

    # Calculate the two solutions
    solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
    solution2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return solution1, solution2