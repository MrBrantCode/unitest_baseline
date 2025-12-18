"""
QUESTION:
Create a function named `fill_jagged_array` that fills a jagged 2D array with zeros. The function takes two parameters: `rows`, the number of inner arrays, and `cols`, a list where each element represents the length of the corresponding inner array. The function must use a single loop and cannot use any built-in array or matrix functions.
"""

def fill_jagged_array(rows, cols):
    """
    Fills a jagged 2D array with zeros.

    Args:
    rows (int): The number of inner arrays.
    cols (list): A list where each element represents the length of the corresponding inner array.

    Returns:
    list: A jagged 2D array filled with zeros.
    """
    jagged_array = []
    for row in range(rows):
        inner_array = [0] * cols[row]
        jagged_array.append(inner_array)
    return jagged_array