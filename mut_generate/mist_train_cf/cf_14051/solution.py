"""
QUESTION:
Write a function called `calculate_sum` that takes an array of positive integers as input and returns their sum without using built-in array methods or loops, only using recursion. The input array is guaranteed to contain only positive integers.
"""

def calculate_sum(arr):
    """
    This function calculates the sum of an array of positive integers using recursion.

    Args:
        arr (list): A list of positive integers.

    Returns:
        int: The sum of the integers in the array.
    """
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])