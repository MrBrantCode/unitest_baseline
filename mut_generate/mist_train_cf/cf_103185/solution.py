"""
QUESTION:
Create a function called `merge_unique_elements` that takes two arrays as input and returns a new array containing unique elements from both input arrays. The function should combine the elements of the two input arrays and eliminate duplicates. The order of the elements in the output array does not matter.
"""

def merge_unique_elements(array1, array2):
    """
    This function merges two arrays and returns a new array containing unique elements.

    Args:
        array1 (list): The first input array.
        array2 (list): The second input array.

    Returns:
        list: A new array containing unique elements from both input arrays.
    """
    return list(set(array1 + array2))