"""
QUESTION:
Create a function `transform_matrix(matrix)` that transforms a given two-dimensional matrix into a one-dimensional list. The list should contain the diagonal elements from the matrix in their respective order, followed by all non-repeated non-diagonal elements. The function should be efficient for large matrices and handle integer elements ranging from -10^9 to 10^9.
"""

def entrance(matrix):
    # Extracting the diagonal elements
    diagonals = [matrix[i][i] for i in range(len(matrix))]

    # Extracting the non diagonal unique elements
    non_diagonals = list(set([element for row in matrix for element in row]) - set(diagonals))

    return diagonals + non_diagonals