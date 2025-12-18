"""
QUESTION:
Write a function named `solve_equations` to solve the system of linear equations -3x + 2y - z = 1, 2x - 2y + 4z = -6, -x + 0.5y - z = 0 and plot the solution on a 3D graph. The function should use numpy to solve the system of equations and matplotlib to plot the solution. The coefficients and constants should be passed as numpy arrays, with the coefficients of x, y, and z in one array and the constants in another. The function should return the solution as a 3D scatter plot.
"""

import numpy as np

def solve_equations(coeff, constant):
    """
    Solve a system of linear equations and return the solution.
    
    Parameters:
    coeff (numpy array): A 2D array of coefficients for the variables in the equations.
    constant (numpy array): A 1D array of constants for the equations.
    
    Returns:
    solution (numpy array): A 1D array containing the values of the variables that solve the system of equations.
    """
    return np.linalg.solve(coeff, constant)