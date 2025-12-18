"""
QUESTION:
Create a function `rotate_2D_matrix(matrix, degree)` that rotates a given NxN 2D matrix counter-clockwise by a specified degree. The degree must be a multiple of 90. The function should handle edge cases where the input matrix is empty or not a square matrix. If the degree is not a multiple of 90, the function should indicate an error. The function should also handle cases where the degree is greater than 360.
"""

import numpy as np

def rotate_2D_matrix(matrix, degree):
    if len(matrix) == 0:
        print("Matrix is empty, cannot perform any rotation.")
        return
    
    row_num = len(matrix)
    col_num = len(matrix[0])
    
    if row_num != col_num:
        print("Invalid Input: Please provide a NxN matrix.")
        return
    
    if degree % 90 != 0:
        print("Invalid Input: Please provide a degree that is a multiple of 90.")
        return

    num_of_rotation = (degree // 90) % 4
      
    for _ in range(num_of_rotation):
        matrix = np.rot90(matrix, axes=(1,0)) 
 
    return matrix