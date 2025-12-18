"""
QUESTION:
We have 3 equations with 3 unknowns x, y, and z and we are to solve for these unknowns.
Equations 4x -3y +z = -10, 2x +y +3z = 0, and -x +2y -5z = 17 will be passed in as an array of [[4, -3, 1, -10], [2, 1, 3, 0], [-1, 2, -5, 17]] and the result should be returned as an array like [1, 4, -2] (i.e. [x, y, z]).

Note: In C++ do not use new or malloc to allocate memory for the returned variable as allocated memory will not be freed in the Test Cases. Setting the variable as static will do.
"""

import numpy as np

def solve_system_of_equations(equations):
    # Extract the coefficients matrix A and the constants vector B
    A = np.array([eq[:3] for eq in equations])
    B = np.array([eq[3] for eq in equations])
    
    # Solve the system of linear equations Ax = B
    solution = np.linalg.solve(A, B)
    
    # Round the solution to the nearest integer and return as a list
    return [round(x) for x in solution]