"""
QUESTION:
Implement a function `solve_linear_equations` to find the intersection point of two linear equations, y = ax + b and y = cx + d. Use numpy to represent the equations in matrix form Ax=b, where A is a 2x2 matrix of coefficients, x is a 2x1 vector of variables, and b is a 2x1 vector of constants. The function should return the solution (x, y) and validate it by checking if the solution satisfies both original equations using numpy's allclose function. The coefficients a, b, c, and d will be provided as input to the function.
"""

import numpy as np

def solve_linear_equations(a, b, c, d):
    """
    This function finds the intersection point of two linear equations, y = ax + b and y = cx + d.
    
    Parameters:
    a (float): coefficient of x in the first equation
    b (float): constant term in the first equation
    c (float): coefficient of x in the second equation
    d (float): constant term in the second equation
    
    Returns:
    tuple: The solution (x, y) to the system of linear equations, and a boolean indicating whether the solution satisfies both equations.
    """
    
    # Define matrix A
    A = np.array([[a, -1], [c, -1]])
    
    # Define matrix B
    B = np.array([-b, -d])
    
    # Find the solution
    solution = np.linalg.solve(A, B)
    
    # Validate the solution
    check_1 = np.allclose(solution[1], a*solution[0] + b)
    check_2 = np.allclose(solution[1], c*solution[0] + d)
    
    return solution[0], solution[1], check_1 and check_2