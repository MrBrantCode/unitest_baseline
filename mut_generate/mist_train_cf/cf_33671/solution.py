"""
QUESTION:
Implement a function `evaluateExpression` that takes an integer `n` representing the size of a square matrix and an array of strings `code` representing a code snippet for a mathematical expression involving matrices. The expression uses the `ma` function to access and the `mb` function to assign values to the matrix. The function should return the result of evaluating the given expression.

The `ma` function takes two indices `i` and `j` and returns the value at the corresponding position in the matrix. The `mb` function takes three arguments: row index `i`, column index `j`, and the value to be assigned to the specified position in the matrix.

Note that the expression will be executed to fill the matrix, and the function should return the value at position (1, 1) in the matrix as the result of the expression evaluation.
"""

def evaluateExpression(n, code):
    matrices = [[0 for _ in range(n)] for _ in range(n)]

    def ma(i, j):
        return matrices[i][j]

    def mb(i, j, val):
        matrices[i][j] = val

    for line in code:
        exec(line)

    return matrices[1][1]