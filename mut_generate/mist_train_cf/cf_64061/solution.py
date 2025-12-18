"""
QUESTION:
Write a function `determinant(matrix)` that calculates the determinant of a given square matrix. The matrix is represented as a 2D list of numbers. The function should return the determinant value if the matrix is square, otherwise it should return an error message "Error: Matrix must be square". The function should also handle edge cases such as empty matrix and single value matrix (1x1).
"""

def determinant(matrix, level=0, accumulator=1.0):
    if len(matrix) == 0:
        # Empty matrix
        return None
    elif len(matrix) == 1:
        # Single value matrix (1x1)
        return matrix[0][0]
    
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
         return "Error: Matrix must be square"

    # Base case for this recursive function:
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Calculate the determinant via recursion:
    result = 0.0
    for i, val in enumerate(matrix[0]):
        newMatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        result += (-1) ** i * val * determinant(newMatrix, level+1, accumulator * len(matrix))
    return result