"""
QUESTION:
Create a function named `calc_det_sarrus(matrix)` that takes a 3x3 matrix as input and returns its determinant using the method of Sarrus. The function should perform the necessary multiplications and subtractions as per the Sarrus rule to calculate the determinant.
"""

def calc_det_sarrus(matrix):
    return ((matrix[0][0]*matrix[1][1]*matrix[2][2]) + 
            (matrix[0][1]*matrix[1][2]*matrix[2][0]) + 
            (matrix[0][2]*matrix[1][0]*matrix[2][1]) -
            (matrix[0][2]*matrix[1][1]*matrix[2][0]) -
            (matrix[0][1]*matrix[1][0]*matrix[2][2]) -
            (matrix[0][0]*matrix[1][2]*matrix[2][1]))