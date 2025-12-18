"""
QUESTION:
Write a function `solve_quadratic` that takes three numerical parameters `a`, `b`, and `c` as input, representing the coefficients of a second-degree polynomial equation `ax^2 + bx + c = 0`. The function should return the two solutions of the equation using the quadratic formula. The function should handle both real and complex solutions.
"""

import cmath  # used to perform complex square root

def solve_quadratic(a, b, c):
    """
    Returns the two solutions of the quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    a (float): The coefficient of the quadratic term.
    b (float): The coefficient of the linear term.
    c (float): The constant term.
    
    Returns:
    tuple: A tuple of two complex numbers representing the solutions of the equation.
    """
    # calculate the discriminant
    D = (b**2) - (4*a*c)
    
    # find two solutions
    sol1 = (-b-cmath.sqrt(D))/(2*a)
    sol2 = (-b+cmath.sqrt(D))/(2*a)
    
    return sol1, sol2