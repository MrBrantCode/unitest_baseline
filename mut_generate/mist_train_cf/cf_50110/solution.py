"""
QUESTION:
Develop a function named `sort_matrix` that takes a square matrix as input and returns a new matrix. The function should leave the odd-numbered rows of the new matrix unchanged and rearrange the values of the even-numbered rows in ascending order. Additionally, calculate the sum of even and odd rows separately. If the sum of all the odd rows is less than the sum of the even rows, sort the entire matrix in ascending order, regardless of row position. The function should return the resulting matrix. The matrix is zero-indexed, with the first row considered as an odd row.
"""

def sort_matrix(matrix):
    # Rearrange even rows
    for i in range(len(matrix)):
        if i % 2 != 0:
            matrix[i] = sorted(matrix[i])

    # Calculate sum of odd and even rows
    odd_rows_sum = sum(sum(row) for i, row in enumerate(matrix) if i % 2 == 0)
    even_rows_sum = sum(sum(row) for i, row in enumerate(matrix) if i % 2 != 0)

    # If sum of even rows > sum of odd rows, sort all rows
    if even_rows_sum > odd_rows_sum:
        matrix = [sorted(row) for row in matrix]

    return matrix