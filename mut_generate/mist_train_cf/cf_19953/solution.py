"""
QUESTION:
Write a recursive Python function named `sum_positive_even` that takes an array of at least 5 integers as input. The function should return the sum of all positive even numbers in the array. If the array does not contain any positive even numbers, the function should return 0.
"""

def sum_positive_even(arr):
    """
    This function calculates the sum of all positive even numbers in an array.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The sum of all positive even numbers in the array. If no positive even numbers are found, returns 0.
    """
    if len(arr) == 0:
        return 0
    
    if arr[0] > 0 and arr[0] % 2 == 0:
        return arr[0] + sum_positive_even(arr[1:])
    else:
        return sum_positive_even(arr[1:])