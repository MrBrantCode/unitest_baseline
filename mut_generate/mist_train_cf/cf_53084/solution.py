"""
QUESTION:
Create a function called `max_in_column` that takes a 2D list `matrix` and an integer `n` as input, where `n` is the index of a column (0-indexed). The function should return the maximum value present in the specified `n`th column of the matrix.
"""

def max_in_column(matrix, n):
    """
    Returns the maximum value present in the specified nth column of the matrix.
    
    Parameters:
    matrix (list): A 2D list of numbers.
    n (int): The index of the column (0-indexed).
    
    Returns:
    The maximum value in the specified column.
    """
    column = [row[n] for row in matrix]
    return max(column)