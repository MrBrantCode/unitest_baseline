"""
QUESTION:
Rotate a 2D array 90 degrees clockwise. The function should take a 2D list of integers as input and return a new 2D list with the rotated array. The input array can be of any size, but it will always be a square (i.e., have the same number of rows and columns). The function should not modify the original array.
"""

def rotate_90(arr):
    """
    Rotate a 2D array 90 degrees clockwise.
    
    Args:
        arr (list): A 2D list of integers.
    
    Returns:
        list: A new 2D list with the rotated array.
    """
    return [list(reversed(i)) for i in zip(*arr)]