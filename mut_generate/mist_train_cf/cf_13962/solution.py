"""
QUESTION:
Write a function named `matrix_multiplication` that takes two matrices M1 and M2 as input and returns their product. The number of columns in M1 must be equal to the number of rows in M2. The resulting matrix should have the same number of rows as M1 and the same number of columns as M2. Both input matrices must be at least 2x2.
"""

def matrix_multiplication(M1, M2):
    rows_M1 = len(M1)
    cols_M1 = len(M1[0])
    rows_M2 = len(M2)
    cols_M2 = len(M2[0])

    # Check if the matrices have compatible sizes for multiplication
    if cols_M1 != rows_M2 or rows_M1 < 2 or rows_M2 < 2 or cols_M1 < 2 or cols_M2 < 2:
        print("Invalid input matrices size for multiplication.")
        return None

    # Initialize the resulting matrix with zeros
    result = [[0] * cols_M2 for _ in range(rows_M1)]

    # Perform matrix multiplication
    for i in range(rows_M1):
        for j in range(cols_M2):
            for k in range(cols_M1):
                result[i][j] += M1[i][k] * M2[k][j]

    return result