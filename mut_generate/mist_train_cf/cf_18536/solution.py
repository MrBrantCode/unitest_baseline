"""
QUESTION:
Write a function `access_element_3d_array` that accesses the third element in the second row of a three-dimensional array. The function should have a constant time complexity, O(1), as it should be able to access the element by its indices regardless of the size of the array.
"""

def access_element_3d_array(three_d_array):
    """
    Access the third element in the second row of a three-dimensional array.

    Args:
        three_d_array (list): A 3D array.

    Returns:
        The third element in the second row of the array.

    Time complexity: O(1)
    """
    return three_d_array[1][0][2]