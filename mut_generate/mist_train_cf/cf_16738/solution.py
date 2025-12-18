"""
QUESTION:
Create a function named `fill_jagged_array_with_zeros` that fills a jagged 2D array with zeros without using any built-in functions or methods. The function should take two parameters: `rows`, which represents the number of inner arrays, and `cols`, which is a list holding the length of each inner array. The function should return the filled jagged 2D array.
"""

def fill_jagged_array_with_zeros(rows, cols):
    """
    Fills a jagged 2D array with zeros without using any built-in functions or methods.

    Args:
        rows (int): The number of inner arrays.
        cols (list): A list holding the length of each inner array.

    Returns:
        list: The filled jagged 2D array.
    """
    jagged_array = []
    for row in range(rows):
        inner_array = []
        for col in range(cols[row]):
            inner_array.append(0)
        jagged_array.append(inner_array)
    return jagged_array