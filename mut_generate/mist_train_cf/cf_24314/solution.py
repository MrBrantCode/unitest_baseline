"""
QUESTION:
Sort a given matrix in such a way that the elements in each row are in increasing order. The function should take a 2D list (matrix) as input and return a new 2D list where each row is sorted.
"""

def sort_matrix(matrix):
    """
    Sorts a given matrix in such a way that the elements in each row are in increasing order.
    
    Args:
        matrix (list): A 2D list of integers.
    
    Returns:
        list: A new 2D list where each row is sorted.
    """
    return [sorted(row) for row in matrix]