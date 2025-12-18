"""
QUESTION:
Create a function named `rotation_matrix` that takes an angle in radians as input and returns a 3x3 rotation matrix. Additionally, create a function named `multiply_matrices` that takes two 3x3 matrices as input and returns the resulting matrix from multiplying the two input matrices together. The rotation matrix should be calculated using trigonometric functions (sine and cosine), and the matrix multiplication should be implemented using the standard matrix multiplication algorithm.
"""

def rotation_matrix(angle):
    return [[math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle),  math.cos(angle), 0],
            [0,              0,              1]]

def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result