"""
ORIGINAL QUESTION:
Implement a function `find_indices_and_average(x, arr)` that takes an integer `x` and a list of integers `arr` as input. The function should return the element at the average index of all occurrences of `x` in `arr` if the average index is a whole number, and -1 otherwise. If `x` does not occur in `arr`, the function should also return -1. The function should only use one loop and not utilize built-in Python array functions such as `count()` and `index()`.
"""

def find_indices_and_average(x, arr):
    """
    This function calculates the average index of all occurrences of x in arr.
    If the average index is a whole number, it returns the element at that index.
    Otherwise, it returns -1. If x does not occur in arr, it also returns -1.

    Parameters:
    x (int): The target number to be searched in the array.
    arr (list): The list of integers.

    Returns:
    int: The element at the average index if it's a whole number, -1 otherwise.
    """
    indices = []
    for i, num in enumerate(arr):
        if num == x:
            indices.append(i)
            
    if len(indices) == 0:
        return -1

    average_index = sum(indices) / len(indices)
    
    if average_index.is_integer():
        return arr[int(average_index)]
    else:
        return -1