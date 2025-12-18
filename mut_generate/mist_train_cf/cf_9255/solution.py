"""
QUESTION:
Create a function `createAlternatingArray` that generates a 2-D array of a given size filled with a pattern of alternating 1's and 0's, starting with 1 in the top left corner. The size of the array is specified by the number of rows and columns, both of which are positive integers.
"""

def createAlternatingArray(rows, cols):
    """
    Creates a 2-D array of a given size filled with a pattern of alternating 1's and 0's,
    starting with 1 in the top left corner.

    Args:
        rows (int): The number of rows in the array.
        cols (int): The number of columns in the array.

    Returns:
        list: A 2-D array filled with alternating 1's and 0's.
    """
    array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                array[i][j] = 1
    return array