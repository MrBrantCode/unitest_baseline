"""
QUESTION:
Write a function `remove_last_item` that takes an array of integers as input and returns the modified array with the last item removed. The function cannot use any built-in array methods or functions such as `pop()` or `slice()` to remove the last item.
"""

def remove_last_item(arr):
    """
    Removes the last item from the given array without using built-in array methods or functions.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The modified array with the last item removed.
    """
    # Check if the array is empty
    if len(arr) == 0:
        return arr
    
    # Create a new array with all elements except the last one
    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append(arr[i])
    
    return new_arr