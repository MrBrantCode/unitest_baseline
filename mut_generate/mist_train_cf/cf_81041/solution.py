"""
QUESTION:
Write a function `add_matrices(a, b)` that takes two matrices `a` and `b` with the same dimensions as input, adds them together, and returns the result as a new matrix. The function should handle sparse matrices efficiently, where some elements in the matrices may be zero. The input matrices are represented as lists of lists in Python.
"""

def add_matrices(a, b):
    # check if matrices are empty
    if len(a) == 0 or len(b) == 0:
        return []

    # get dimensions
    rows = len(a)
    columns = len(a[0])

    # create a new matrix for the result with same dimensions
    result = [[0 for _ in range(columns)] for _ in range(rows)]

    # iterate through matrices
    for i in range(rows):
        for j in range(columns):
            # only perform addition if both elements are not zero (sparse scenario)
            if a[i][j] != 0 or b[i][j] != 0:
                result[i][j] = a[i][j] + b[i][j]

    return result