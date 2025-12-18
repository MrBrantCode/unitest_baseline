"""
QUESTION:
Write a function `circular_rotate_3d_matrix` that takes a 3D matrix as input and performs a circular rotation on it. The function should return the rotated 3D matrix. The input 3D matrix is a 3-dimensional list of integers, and the rotation should be performed by moving the last 2D matrix to the front of the 3D matrix. The function should not use any external libraries.
"""

def circular_rotate_3d_matrix(mat_3d):
    """
    Perform a circular rotation on a 3D matrix by moving the last 2D matrix to the front.

    Args:
        mat_3d (list): A 3-dimensional list of integers.

    Returns:
        list: The rotated 3D matrix.
    """
    return [mat_3d[-1]] + mat_3d[:-1]