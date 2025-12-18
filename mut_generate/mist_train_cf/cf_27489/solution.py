"""
QUESTION:
Implement a function `solve_linear_equations(A, b)` that solves a system of linear equations represented by the input matrix `A` and vector `b`, where `A` is a 2D matrix representing the coefficients of the linear equations and `b` is a 1D vector representing the constants on the right-hand side of the equations. The function should return a list of solutions if a unique solution exists, otherwise, return a message indicating that no unique solution exists.
"""

import numpy as np

def solve_linear_equations(A, b):
    if np.linalg.matrix_rank(A) == A.shape[1]:
        solution = np.linalg.solve(A, b)
        return solution.tolist()
    else:
        return "No unique solution exists for the given system of equations."