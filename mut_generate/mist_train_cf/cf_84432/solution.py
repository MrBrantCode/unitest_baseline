"""
QUESTION:
Create a function `calculate_determinant(matrix)` that takes a 2D list of integers or floats (representing a square matrix) as input and returns its determinant. The function should handle matrices of any size, but it is expected to work efficiently for small to medium-sized matrices.
"""

def calculate_determinant(matrix):
    # If it's a 1x1 matrix, return the sole element
    if len(matrix) == 1:
        return matrix[0][0]
    
    # If it's a 2x2 matrix, return ad - bc
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    # Compute the determinant
    for j in range(len(matrix[0])):
        # Exclude first row and jth column
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Sign of the cofactor flips for each j
        # We add one to j to account for the fact that we excluded the first row
        sign = (-1) ** (j % 2)
        # Recursively compute the determinant
        determinant += sign * matrix[0][j] * calculate_determinant(sub_matrix)

    return determinant