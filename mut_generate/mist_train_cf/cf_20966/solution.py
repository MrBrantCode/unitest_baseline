"""
QUESTION:
Write a function `bubble_sort_matrix(matrix, ascending=True)` that sorts a two-dimensional array (matrix) using bubble sort. The matrix contains a mix of positive and negative integers, and each row may have a different number of elements. The function should take an optional parameter `ascending` that defaults to `True`, which determines the sorting order (ascending if `True`, descending if `False`). The function should handle edge cases such as empty matrices and matrices with only one row or one column.
"""

def bubble_sort_matrix(matrix, ascending=True):
    rows = len(matrix)
    if rows == 0:  # empty matrix
        return matrix
    
    cols = len(matrix[0])
    if cols == 0:  # empty row
        return matrix
    
    for i in range(rows):
        for j in range(cols - 1):
            for k in range(cols - j - 1):
                if (ascending and matrix[i][k] > matrix[i][k+1]) or (not ascending and matrix[i][k] < matrix[i][k+1]):
                    matrix[i][k], matrix[i][k+1] = matrix[i][k+1], matrix[i][k]
    
    return matrix