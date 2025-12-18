"""
QUESTION:
Create a function named `rotate_right` that takes two inputs: a list of elements (`array`) and the number of steps to rotate (`steps`). Rotate the elements in the array to the right by the specified number of steps and return the resulting array.
"""

def rotate_right(array, steps):
    """
    Rotate the elements in the array to the right by the specified number of steps.

    Args:
    array (list): A list of elements to be rotated.
    steps (int): The number of steps to rotate the array.

    Returns:
    list: The resulting array after rotation.
    """
    return array[-steps:] + array[:-steps]