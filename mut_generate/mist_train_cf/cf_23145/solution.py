"""
QUESTION:
Create a function `find_max_slices` that takes a 3D array of size 5x5x5 as input, where each element is a positive integer. The function should return a 2D array where each element represents the maximum value in the corresponding 2D slice of the input 3D array.
"""

def find_max_slices(array_3d):
    """
    This function takes a 3D array of size 5x5x5 as input, 
    where each element is a positive integer. It returns a 2D array 
    where each element represents the maximum value in the corresponding 
    2D slice of the input 3D array.

    Args:
        array_3d (list): A 3D array of size 5x5x5.

    Returns:
        list: A 2D array where each element is the maximum value in the 
        corresponding 2D slice of the input 3D array.
    """
    max_slices = []
    for array_2d in array_3d:
        max_values = [max(array_1d) for array_1d in array_2d]
        max_slices.append(max_values)
    return max_slices