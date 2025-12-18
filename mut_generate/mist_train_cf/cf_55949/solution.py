"""
QUESTION:
Write a function called `solve_linear_equations` that solves a system of three linear equations with three unknowns (x, y, z) and returns the solutions for x, y, and z as rational numbers. The system of equations is represented by a 3x3 matrix A of coefficients and a 1x3 vector B of constants. The function should use NumPy's linear algebra functions to solve the system of equations and the fractions library to express the solutions as rational numbers. The function should also include a test to validate the correctness of the solution. 

Restrictions: The system of equations must be consistent and have a unique solution.
"""

import numpy as np
from fractions import Fraction

def solve_linear_equations(A, B):
    """
    Solves a system of three linear equations with three unknowns (x, y, z) 
    and returns the solutions for x, y, and z as rational numbers.

    Args:
    A (numpy array): A 3x3 matrix of coefficients from the left-hand side of the equations.
    B (numpy array): A 1x3 vector from the right-hand side of the equations.

    Returns:
    A tuple of three rational numbers representing the solutions for x, y, and z.

    Raises:
    AssertionError: If the system of equations is not consistent or does not have a unique solution.
    """
    X = np.linalg.solve(A, B)
    assert np.allclose(np.dot(A, X), B), "The solution is not correct"
    return (Fraction(X[0]).limit_denominator(), 
            Fraction(X[1]).limit_denominator(), 
            Fraction(X[2]).limit_denominator())