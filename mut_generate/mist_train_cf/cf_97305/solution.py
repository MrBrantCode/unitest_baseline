"""
QUESTION:
Implement a function `add_matrices(matrix1, matrix2)` that adds two matrices of the same size using recursion. The function should take two 2D lists `matrix1` and `matrix2` as input, where the number of rows and columns in both matrices are the same. The function should return a new 2D list representing the sum of the input matrices.
"""

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    columns = len(matrix1[0])

    result = [[0 for _ in range(columns)] for _ in range(rows)]

    def add_elements(i, j):
        if i >= rows:
            return

        if j >= columns:
            return add_elements(i + 1, 0)

        result[i][j] = matrix1[i][j] + matrix2[i][j]
        add_elements(i, j + 1)

    add_elements(0, 0)
    return result