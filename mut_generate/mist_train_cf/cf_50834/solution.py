"""
QUESTION:
Create a function `solve_system(equations)` that takes a list of three string equations as input, where each equation represents a linear equation with three variables (x, y, z) and is in the format of 'a b c=d', with coefficients a, b, c, and d being integers, and a space separating each coefficient. The function should return a dictionary containing the values of x, y, and z that solve the system of equations, or a message indicating that the system has no solution. The function should also handle cases where the system of equations has no solution, and should return decimal approximations of the solution values.
"""

import numpy as np

def solve_system(equations):
    coefficients, solutions = zip(*[eq.split('=') for eq in equations])
    coefficients = np.array([list(map(int, coef.split())) for coef in coefficients])
    solutions = np.array(list(map(int, solutions)))[:, np.newaxis]

    try:
        solutions = np.linalg.solve(coefficients, solutions).flatten().tolist()
        return dict(zip(['x', 'y', 'z'], solutions))
    except np.linalg.LinAlgError:
        return "This system of equations has no solutions."