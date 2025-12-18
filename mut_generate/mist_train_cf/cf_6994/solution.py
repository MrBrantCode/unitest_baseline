"""
QUESTION:
Create a function called `angle_to_rotation_matrix` that takes an angle in degrees as input and returns a 3x3 rotation matrix. The function should use the trigonometric functions (sine and cosine) to calculate the values for each element of the rotation matrix. The top left element should be cosine(angle), the top middle element should be -sine(angle), the bottom left element should be sine(angle), the bottom right element should be cosine(angle), and the middle elements should be 0.

Create another function called `multiply_matrices` that takes two 3x3 matrices as input and returns the resulting matrix after multiplication. The function should implement the matrix multiplication algorithm, which involves multiplying corresponding elements of the matrices and summing the results.

The input angle should be in degrees and the trigonometric functions should be used with the angle in radians. The rotation matrix should be a 3x3 matrix and the multiplication result should also be a 3x3 matrix.
"""

import math

# Function to convert angle in degrees to a 3x3 rotation matrix
def angle_to_rotation_matrix(angle):
    angle_rad = math.radians(angle)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    rotation_matrix = [[cos_theta, -sin_theta, 0],
                       [sin_theta, cos_theta, 0],
                       [0, 0, 1]]
    return rotation_matrix

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result