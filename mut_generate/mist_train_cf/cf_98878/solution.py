"""
QUESTION:
Create a function called `solve_linear_equations` that solves a system of linear equations. The function should take in a 2D list `coefficients` representing the coefficients of the unknown variables and a list `constants` representing the constants on the right-hand side of the equations. The function should return the solution as a list of values for the unknown variables. The function should use the `numpy` package to solve the system of equations.
"""

import numpy as np

def solve_linear_equations(coefficients, constants):
    """
    Solves a system of linear equations.

    Parameters:
    coefficients (2D list): Coefficients of the unknown variables.
    constants (list): Constants on the right-hand side of the equations.

    Returns:
    list: Solution as a list of values for the unknown variables.
    """
    A = np.array(coefficients)
    B = np.array(constants)
    return np.linalg.solve(A, B)