"""
QUESTION:
Create a function called `reverse_sorted_array` that takes an array of strings as input, sorts the array in alphabetical order, and returns the reverse of the sorted array. The input array contains only strings.
"""

def reverse_sorted_array(arr):
    """
    This function takes an array of strings, sorts it in alphabetical order, 
    and returns the reverse of the sorted array.

    Args:
        arr (list): A list of strings.

    Returns:
        list: The reverse of the sorted array.
    """
    return sorted(arr)[::-1]