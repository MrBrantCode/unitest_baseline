"""
QUESTION:
Write a function called `solve_linear_equations` that takes two pairs of coefficients (a1, b1, c1) and (a2, b2, c2) representing two linear equations in the form a1x + b1y = c1 and a2x + b2y = c2. The function should return a solution for x and y if the lines are not parallel. If the lines are parallel, the function should return a message stating that the lines are parallel and there is no solution.
"""

import numpy as np

def solve_linear_equations(a1, b1, c1, a2, b2, c2):
    """
    Solves a system of two linear equations in the form a1x + b1y = c1 and a2x + b2y = c2.
    
    Args:
    a1, b1, c1 (float): Coefficients of the first equation.
    a2, b2, c2 (float): Coefficients of the second equation.
    
    Returns:
    tuple: A tuple containing the solution (x, y) if the lines are not parallel. 
           Otherwise, returns a message stating that the lines are parallel and there is no solution.
    """
    # Coefficients Matrix (A)
    A = np.array([[a1, b1], [a2, b2]])
    
    # Results Matrix (B)
    B = np.array([c1, c2])
    
    # Check if lines are parallel (Determinant of A is zero)
    if np.linalg.det(A) == 0:
        return "The lines are parallel. No solution."
    else:
        # Solve for the variables
        solution = np.linalg.solve(A, B)
        return solution