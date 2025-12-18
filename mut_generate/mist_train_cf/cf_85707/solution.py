"""
QUESTION:
Write a function `print_diagonal_zigzag` that takes a 2D list `matrix` of variable row and column lengths as input and returns its elements in a zigzag diagonal order. The function should handle edge cases where the matrix has zero rows or columns, or where the matrix has only one row or column.
"""

def print_diagonal_zigzag(matrix):
    if len(matrix) == 0 or len(matrix[0])==0:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []
    row = col = 0
    
    for _ in range(m * n):
        result.append(matrix[row][col])
        if (row + col) % 2 == 0: # moving up
            if col == n - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else: # moving down
            if row == m - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1

    return result