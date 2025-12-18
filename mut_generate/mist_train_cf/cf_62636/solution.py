"""
QUESTION:
Develop a function `sum_of_square_diagonal_elements(matrix)` to calculate the sum of the square of unique diagonal elements in a given square matrix. The function should handle and return error messages for non-square matrices, empty matrices, and matrices containing non-numeric values. The matrix is guaranteed to have a maximum dimension of 100x100, and both the principal and secondary diagonal elements should be considered.
"""

def sum_of_square_diagonal_elements(matrix):
    # Check if matrix is not empty
    if not matrix:
        return "Error: The matrix is empty."
  
    # Get the row and col lengths
    row_length = len(matrix)
    col_length = len(matrix[0])
  
    # Check if the matrix is a square matrix
    if row_length != col_length:
        return "Error: The matrix is not a square matrix."
  
    # Set to hold unique diagonal elements
    diagonal_elements = set()
  
    for i in range(row_length):
        for j in range(col_length):
            # Check if each element is a number
            if not isinstance(matrix[i][j], (int, float)):
                return "Error: The matrix contains non-numeric values."
            # Check if it's a principal or secondary diagonal element
            if i == j or i + j == row_length - 1:
                diagonal_elements.add(matrix[i][j])
  
    # Calculate and return sum of square of unique diagonal elements
    return sum(e ** 2 for e in diagonal_elements)