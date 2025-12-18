"""
QUESTION:
Create a function `find_max_divisible_by_3` that takes a 3D array as input and returns a 1D array where each element represents the maximum value divisible by 3 in the corresponding 2D slice. The function should only consider elements that are divisible by 3 when finding the maximum value in each 2D slice. The input 3D array is of size 5x5x5, and each element is a randomly generated positive integer between 1 and 1000.
"""

def find_max_divisible_by_3(array_3d):
    """
    This function takes a 3D array as input and returns a 1D array where each element represents 
    the maximum value divisible by 3 in the corresponding 2D slice.

    Args:
        array_3d (list): A 3D array of size 5x5x5 with positive integers.

    Returns:
        list: A 1D array with the maximum value divisible by 3 in each 2D slice.
    """

    max_values = []
    for slice_2d in array_3d:
        max_value = 0
        for row in slice_2d:
            for element in row:
                if element % 3 == 0 and element > max_value:
                    max_value = element
        max_values.append(max_value)
    return max_values