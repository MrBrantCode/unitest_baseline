"""
QUESTION:
Write a function `create_2d_array` to declare and initialize a 2D array. The dimensions of the array should be obtained from user input and should not exceed 100x100. The function should return the created 2D array. The array should be filled with integers where each element is the column number plus one.
"""

def create_2d_array(rows, cols):
    """
    Creates a 2D array with the specified dimensions and fills it with integers.
    
    Each element in the array is the column number plus one.

    Args:
        rows (int): The number of rows in the array.
        cols (int): The number of columns in the array.

    Returns:
        list: A 2D array with the specified dimensions and filled with integers.
    """
    return [[j + 1 for j in range(cols)] for _ in range(rows)]