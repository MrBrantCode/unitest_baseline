"""
QUESTION:
Create a function `display_elements` that takes a 3D matrix as input and returns a list of its elements in order. The function should be optimized for performance, especially when dealing with large matrices.
"""

def display_elements(matrix):
    """
    This function takes a 3D matrix as input and returns a list of its elements in order.

    Args:
        matrix (list): A 3D list of lists of lists.

    Returns:
        list: A list of elements in the 3D matrix.
    """
    return [item for sublist1 in matrix for sublist2 in sublist1 for item in sublist2]