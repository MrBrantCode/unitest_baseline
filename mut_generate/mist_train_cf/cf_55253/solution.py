"""
QUESTION:
Design a function `remove(data, position)` that takes a three-dimensional array `data` and a list of indices `position` as input, removes the element at the specified position from the array, and returns the updated array. If the indices in `position` are out-of-bounds, the function should return an error message. The function should also maintain the relative order of the remaining elements in the array.
"""

def remove(data, position):
    """
    Removes the element at the specified position from the 3D array.

    Args:
        data (list): A 3D array.
        position (list): A list of indices.

    Returns:
        list: The updated 3D array or an error message if the indices are out-of-bounds.
    """
    try:
        del data[position[0]][position[1]][position[2]]
        return data
    except IndexError:
        return "Index out-of-range"