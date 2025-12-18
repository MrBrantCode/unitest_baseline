"""
QUESTION:
Create a function named modify_array that takes a list as input and returns the list with the element at index 4 multiplied by 2. The function should not modify the original list structure, but only the value at index 4.
"""

def modify_array(arr):
    """
    This function takes a list as input, multiplies the element at index 4 by 2, 
    and returns the modified list without altering the original list structure.

    Args:
        arr (list): The input list.

    Returns:
        list: The modified list with the element at index 4 multiplied by 2.
    """
    if len(arr) > 4:  # check if the list has at least 5 elements
        arr = arr[:]  # create a copy of the original list
        arr[4] = arr[4] * 2  # multiply the element at index 4 by 2
    return arr