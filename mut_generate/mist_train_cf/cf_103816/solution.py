"""
QUESTION:
Create a function called `combine_arrays` that takes two 2D arrays as input. Each sub-array contains a string and a number. Combine the two input arrays into one array, sorting the resulting array first by the number in ascending order, and then by the string in descending order.
"""

def combine_arrays(arr1, arr2):
    """
    Combine two 2D arrays and sort the resulting array by number in ascending order, 
    and then by string in descending order.

    Args:
        arr1 (list): The first 2D array.
        arr2 (list): The second 2D array.

    Returns:
        list: The combined and sorted 2D array.
    """
    combined = arr1 + arr2
    combined.sort(key=lambda x: (x[1], x[0].lower()[::-1]))
    return combined