"""
QUESTION:
Write a function named `find_min_max` that takes a 2D list (matrix) of integers as input and returns the minimum and maximum values in the matrix.
"""

def find_min_max(matrix):
    """
    This function finds the minimum and maximum values in a given 2D list (matrix) of integers.
    
    Args:
        matrix (list): A 2D list of integers.
    
    Returns:
        tuple: A tuple containing the minimum and maximum values in the matrix.
    """
    min_val = min(min(row) for row in matrix)
    max_val = max(max(row) for row in matrix)
    return min_val, max_val