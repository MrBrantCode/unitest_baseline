"""
QUESTION:
Given a rectangular 2D array and a 1D index, write a function `access_element` that takes the 2D array and the index as input and returns the element at the corresponding position in the array. The 1D index is calculated based on the row-major ordering of the array, where the elements in the first row are indexed first, followed by the elements in the second row, and so on. Assume that the input index is valid and within the bounds of the array.
"""

def access_element(array, index):
    """
    Access an element in a 2D array based on its 1D index.

    Args:
        array (list of lists): The 2D array.
        index (int): The 1D index of the element.

    Returns:
        The element at the corresponding position in the array.
    """
    num_rows = len(array)
    num_columns = len(array[0])

    row_index = index // num_columns
    column_index = index % num_columns

    return array[row_index][column_index]