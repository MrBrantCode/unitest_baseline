"""
QUESTION:
Write a function `bubble_sort_matrix(matrix, ascending=True)` that sorts a two-dimensional array (matrix) using bubble sort. The function should take a matrix with rows of varying lengths and sort each row in either ascending or descending order based on the `ascending` parameter. The function should handle edge cases such as empty matrices and matrices with only one row or one column.
"""

def bubble_sort_matrix(matrix, ascending=True):
    """
    Sorts a two-dimensional array (matrix) using bubble sort.

    Args:
        matrix (list of lists): A two-dimensional array to be sorted.
        ascending (bool): Sort order. Default is True for ascending order.

    Returns:
        list of lists: The sorted matrix.
    """
    rows = len(matrix)
    if rows == 0:  # empty matrix
        return matrix
    
    for row in matrix:
        cols = len(row)
        if cols == 0:  # empty row
            continue
        
        for j in range(cols - 1):
            for k in range(cols - j - 1):
                if (ascending and row[k] > row[k+1]) or (not ascending and row[k] < row[k+1]):
                    row[k], row[k+1] = row[k+1], row[k]
    
    return matrix