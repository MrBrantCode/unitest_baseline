"""
QUESTION:
Write a function solve_linear_equations to solve a system of two linear equations with three variables. The function should take the coefficients of the two equations as input in the form of two 3-element lists or tuples [a1, b1, c1] and [a2, b2, c2] and the constants of the equations as two numbers d1 and d2, where the equations are in the form a1x + b1y + c1z = d1 and a2x + b2y + c2z = d2. The function should return the values of x, y, and z that satisfy both equations.
"""

import numpy as np

def solve_linear_equations(coefficients1, coefficients2, constant1, constant2):
    """
    Solves a system of two linear equations with three variables.

    Args:
        coefficients1 (list or tuple): Coefficients of the first equation [a1, b1, c1].
        coefficients2 (list or tuple): Coefficients of the second equation [a2, b2, c2].
        constant1 (float): Constant of the first equation.
        constant2 (float): Constant of the second equation.

    Returns:
        tuple: Values of x, y, and z that satisfy both equations.
    """
    A = np.array([coefficients1[:2], coefficients2[:2]])
    B = np.array([constant1, constant2])
    solution = np.linalg.solve(A, B)
    x = solution[0]
    y = solution[1]
    z = (constant1 - coefficients1[0]*x - coefficients1[1]*y) / coefficients1[2]
    return x, y, z