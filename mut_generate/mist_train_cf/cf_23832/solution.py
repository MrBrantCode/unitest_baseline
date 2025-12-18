"""
QUESTION:
Create a function named `create_2d_array` that takes in two parameters: `rows` and `cols`, representing the number of rows and columns in the array. The function should return a 2D array filled with zeros. The array should have the specified number of rows and columns.
"""

def create_2d_array(rows, cols):
    """
    Creates a 2D array filled with zeros.

    Args:
        rows (int): The number of rows in the array.
        cols (int): The number of columns in the array.

    Returns:
        list: A 2D array filled with zeros.
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]