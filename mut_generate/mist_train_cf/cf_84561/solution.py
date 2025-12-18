"""
QUESTION:
Write a function `solve_quadratic` that calculates the solutions to a quadratic equation of the form ax² + bx + c = 0. The function should take three parameters: `a`, `b`, and `c`, which represent the coefficients of the quadratic equation. The function should return the two solutions of the equation. Note that the function should only handle equations with real roots, i.e., the discriminant (b² - 4ac) is non-negative.
"""

import math

def solve_quadratic(a, b, c):
    """
    Calculate the solutions to a quadratic equation of the form ax² + bx + c = 0.

    Args:
        a (float): The coefficient of x².
        b (float): The coefficient of x.
        c (float): The constant term.

    Returns:
        tuple: The two solutions of the equation.
    """
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # two solutions
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)

    return sol1, sol2