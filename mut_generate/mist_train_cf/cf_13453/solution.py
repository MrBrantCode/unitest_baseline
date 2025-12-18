"""
QUESTION:
Create a function called `total_unique_elements` that calculates the total number of unique elements in a given 2D array, where each sub-array contains exactly two positive integers greater than zero. The function should return the total count of unique elements in the array.
"""

def total_unique_elements(array):
    """
    Calculate the total number of unique elements in a given 2D array.

    Args:
    array (list): A 2D array where each sub-array contains exactly two positive integers greater than zero.

    Returns:
    int: The total count of unique elements in the array.
    """
    unique_elements = set()
    for sub_array in array:
        unique_elements.add(sub_array[0])
        unique_elements.add(sub_array[1])
    return len(unique_elements)