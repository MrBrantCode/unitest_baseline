"""
QUESTION:
Write a function named `clone_and_reverse_array` that takes an array as input, clones it, and returns the cloned array with its elements in reverse order. The original array should not be modified. Do not use any built-in array manipulation functions such as reverse or slice.
"""

def clone_and_reverse_array(arr):
    """
    Clones the input array and returns the cloned array with its elements in reverse order.
    
    Args:
        arr (list): The input array.
    
    Returns:
        list: The cloned array with its elements in reverse order.
    """
    cloned_arr = []
    for i in range(len(arr) - 1, -1, -1):
        cloned_arr.append(arr[i])
    return cloned_arr