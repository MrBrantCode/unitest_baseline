"""
QUESTION:
Create a function called `find_lowest_trifecta` that takes an array of integers as input and returns the three smallest numbers in the array. The function should be able to handle arrays of any length, but for this problem, assume the array has at least three elements. The function should not use any external libraries or data structures, only built-in array operations.
"""

def find_lowest_trifecta(arr):
    """
    Returns the three smallest numbers in the input array.

    Args:
    arr (list): A list of integers.

    Returns:
    list: A list of the three smallest integers in the input array.
    """
    # Sort the array in ascending order
    arr.sort()
    
    # Return the first three elements from the sorted array
    return arr[0:3]