"""
QUESTION:
Find the longest diagonal sequence with unique integers in a given matrix.

Given a matrix of integers, write a function `longest_unique_diagonal` that returns the maximum number of unique integers in a diagonal sequence.

Restrictions: The input matrix can contain any number of rows and columns, and the function should handle cases where the matrix contains only one or the same recurring integer.
"""

def longest_unique_diagonal(matrix):
    """
    This function finds the maximum number of unique integers in a diagonal sequence in a given matrix.

    Args:
        matrix (list of lists): A 2D list of integers.

    Returns:
        int: The maximum number of unique integers in a diagonal sequence.
    """
    
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp_table = [[1]*cols for _ in range(rows)]
    
    for col in range(1, cols):
        for row in range(rows):
            this_row, this_col = row - 1, col - 1
            while this_row >= 0 and this_col >= 0:
                if matrix[row][col] == matrix[this_row][this_col]:
                    dp_table[row][col] = max(dp_table[row][col], dp_table[this_row][this_col] + 1)
                this_row -= 1
                this_col -= 1
    
    max_unique = max(max(row) for row in dp_table)
    return max_unique