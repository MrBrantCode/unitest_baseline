"""
QUESTION:
Create a function `add_matrices(matrix1, matrix2)` that adds two matrices of the same size using recursion. The function should take two 2D lists (matrices) as input and return a new 2D list (matrix) where each element is the sum of corresponding elements in the input matrices. The matrices must have the same number of rows and columns, and the function should handle matrices of any size.
"""

def add_matrices(matrix1, matrix2):
    # Get the number of rows and columns of the matrices
    rows = len(matrix1)
    columns = len(matrix1[0])

    # Create a result matrix of the same size as the input matrices
    result = [[0 for _ in range(columns)] for _ in range(rows)]

    # Recursively add corresponding elements of the matrices
    def add_elements(i, j):
        if i >= rows:
            return

        if j >= columns:
            return add_elements(i + 1, 0)

        # Add corresponding elements and store the result in the result matrix
        result[i][j] = matrix1[i][j] + matrix2[i][j]

        # Recursively move to the next element
        add_elements(i, j + 1)

    # Start the recursion
    add_elements(0, 0)

    return result