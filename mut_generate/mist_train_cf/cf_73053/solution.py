"""
QUESTION:
Write a function `compute_C_value(n)` that calculates the sum of the least intricacy of an n x n binary matrix for all possible numbers of ones (from 0 to n^2). The intricacy of a matrix is the count of unique rows and columns. The function should be optimized to handle large inputs like n = 10^4.
"""

def compute_C_value(n):
    """
    This function calculates the sum of the least intricacy of an n x n binary matrix 
    for all possible numbers of ones (from 0 to n^2).
    
    Args:
    n (int): The size of the binary matrix.

    Returns:
    int: The sum of the least intricacy of the matrix.
    """
    C = 0
    for ones in range(n**2 + 1):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(ones):
            matrix[i%n][i//n] = 1
        rows = [''.join(map(str, row)) for row in matrix]
        columns = [''.join(map(str, column)) for column in zip(*matrix)]
        C += len(set(rows + columns))
    return C