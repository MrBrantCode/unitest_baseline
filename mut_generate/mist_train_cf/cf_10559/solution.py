"""
QUESTION:
Write a function called `rearrange_array` that takes a list of integers as input, removes the last three elements, adds them to the beginning of the list, and returns the resulting list in ascending order. If the input list has less than three elements, return the original list.
"""

def rearrange_array(arr):
    """
    This function rearranges the input list by moving the last three elements to the beginning and sorting in ascending order.
    
    If the input list has less than three elements, the original list is returned.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The rearranged list in ascending order.
    """
    if len(arr) < 3:
        return arr
    last_three = arr[-3:]
    arr = last_three + arr[:-3]
    arr.sort()
    return arr