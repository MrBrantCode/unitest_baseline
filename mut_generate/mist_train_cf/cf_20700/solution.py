"""
QUESTION:
Design a function `search_2d_array` that takes a 2D list `matrix` and an integer `target` as input, where the matrix is sorted row-wise and column-wise in non-decreasing order. The function should return the indices (i, j) of the target if found, or a specific value to indicate that it's not in the matrix. The function should achieve this in O(m + n) time complexity, where m and n are the number of rows and columns of the matrix, respectively.
"""

def search_2d_array(matrix, target):
    """
    Searches for a target value in a 2D list sorted row-wise and column-wise in non-decreasing order.

    Args:
        matrix (list): A 2D list of integers sorted row-wise and column-wise in non-decreasing order.
        target (int): The target value to search for.

    Returns:
        tuple: The indices (i, j) of the target if found, or (-1, -1) if not found.
    """

    if not matrix or not matrix[0]:
        return (-1, -1)

    rows, cols = len(matrix), len(matrix[0])
    i, j = 0, cols - 1

    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return (i, j)
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1

    return (-1, -1)