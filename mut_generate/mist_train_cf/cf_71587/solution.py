"""
QUESTION:
Write a function `solve_linear_equations` that solves a system of linear equations using numpy's linalg.solve() method. The function should take as input a 2D list `coefficients` representing the coefficients of the variables in each equation, and a list `constants` representing the constants of each equation. The function should return the solution to the system of linear equations. The system of linear equations is guaranteed to have a unique solution.
"""

import numpy as np

def solve_linear_equations(coefficients, constants):
    """
    Solves a system of linear equations using numpy's linalg.solve() method.

    Parameters:
    coefficients (2D list): Coefficients of the variables in each equation.
    constants (list): Constants of each equation.

    Returns:
    list: The solution to the system of linear equations.
    """
    A = np.array(coefficients)
    b = np.array(constants)
    return np.linalg.solve(A, b)