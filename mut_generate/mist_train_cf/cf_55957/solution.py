"""
QUESTION:
Write a function in Python, using the numpy library, to calculate the determinant of a square matrix. The input will be a 2D list of numbers representing the matrix elements. The function should return the determinant of the matrix.
"""

import numpy as np

def calculate_determinant(matrix):
    """
    Calculate the determinant of a square matrix.
    
    Parameters:
    matrix (list): A 2D list representing the matrix elements.
    
    Returns:
    float: The determinant of the matrix.
    """
    return np.linalg.det(np.array(matrix))