"""
QUESTION:
Write a function `solve_quadratic_equation` that takes three coefficients `a`, `b`, and `c` as input and returns the exact numerical solutions for the variable `y` in the quadratic equation `ay² + by + c = 0`. The function should be able to handle both real and complex solutions.
"""

import cmath

def solve_quadratic_equation(a, b, c):
    """
    This function solves a quadratic equation of the form ax² + bx + c = 0.
    
    Parameters:
    a (float): The coefficient of the squared variable.
    b (float): The coefficient of the variable.
    c (float): The constant term.
    
    Returns:
    tuple: A tuple containing the two solutions for the equation.
    """
    
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    return sol1, sol2