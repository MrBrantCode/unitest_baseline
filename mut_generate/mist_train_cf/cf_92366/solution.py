"""
QUESTION:
Write a function named `get_element_at_index` that takes a 2D list `array` and an integer `index` as input and returns the element at the corresponding position in the 1D representation of the 2D list. The 2D list is a rectangular array, where the index is calculated by iterating over the elements from left to right and top to bottom. Assume the input index is valid.
"""

def get_element_at_index(array, index):
    """
    Returns the element at the corresponding position in the 1D representation of the 2D list.

    Args:
        array (list): A 2D list.
        index (int): The index of the element in the 1D representation.

    Returns:
        The element at the specified index.
    """
    num_rows = len(array)
    num_columns = len(array[0])
    row_index = index // num_columns
    column_index = index % num_columns
    return array[row_index][column_index]