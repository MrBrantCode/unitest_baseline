"""
QUESTION:
Write a function `replace_mirrored_zero(matrix)` that takes a square 2D matrix of alphanumeric elements as input and returns the modified matrix. The function should replace each occurrence of the character '0' with the next ASCII character '1' if the '0' has a mirrored counterpart across the central horizontal and vertical lines of the matrix. If the '0' does not have a mirrored counterpart, it should remain unchanged.
"""

def replace_mirrored_zero(matrix):
    n = len(matrix)
    mid = n // 2

    # check only the first half
    for i in range(mid):
        for j in range(n):
            if matrix[i][j] == '0' and matrix[n - 1 - i][n - 1 - j] == '0':
                matrix[i][j] = matrix[n - 1 - i][n - 1 - j] = chr(ord('0') + 1)
            if matrix[j][i] == '0' and matrix[n - 1 - j][n - 1 - i] == '0':
                matrix[j][i] = matrix[n - 1 - j][n - 1 - i] = chr(ord('0') + 1)

    # check central row/col for odd size matrix
    if n % 2 != 0:
        for i in range(mid):
            if matrix[mid][i] == '0' and matrix[mid][n - 1 - i] == '0':
                matrix[mid][i] = matrix[mid][n - 1 - i] = chr(ord('0') + 1)
            if matrix[i][mid] == '0' and matrix[n - 1 - i][mid] == '0':
                matrix[i][mid] = matrix[n - 1 - i][mid] = chr(ord('0') + 1)

    return matrix