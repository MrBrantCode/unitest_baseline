"""
QUESTION:
Implement a function `calculate_jacobian_determinant(J)` that takes a 2x2 transformation matrix `J` as a 2D array of integers as input and returns the calculated Jacobian determinant `j` as a float. The Jacobian determinant is calculated using the formula `j = 0.5 * det(J)`, where `det(J)` denotes the determinant of matrix `J`.
"""

from typing import List
import numpy as np

def calculate_jacobian_determinant(J: List[List[int]]) -> float:
    # Convert the 2D list to a numpy array for matrix operations
    J_np = np.array(J)
    
    # Calculate the determinant of the transformation matrix
    det_J = np.linalg.det(J_np)
    
    # Calculate the Jacobian determinant using the formula: j = 0.5 * det(J)
    j = 0.5 * det_J
    
    return j