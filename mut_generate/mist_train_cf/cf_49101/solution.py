"""
QUESTION:
Create a function called `custom_sort` that sorts an array of mixed data types in ascending order, with non-string elements coming before string elements. Then, return the last three elements of the sorted array. The function should handle arrays containing a mix of integers, floats, and strings.
"""

def custom_sort(arr):
    """
    Sorts an array of mixed data types in ascending order, 
    with non-string elements coming before string elements.
    
    Args:
    arr (list): The input array containing mixed data types.
    
    Returns:
    list: The last three elements of the sorted array.
    """
    return sorted(arr, key=lambda x: (isinstance(x, str), x))[-3:]