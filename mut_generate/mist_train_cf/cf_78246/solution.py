"""
QUESTION:
Write a function named `average` that calculates and returns the average of all elements in a given array of numbers. The function should return 0 if the array is empty. The array may only contain numbers, and the function does not need to handle arrays with non-numeric elements.
"""

def average(arr):
    """
    This function calculates and returns the average of all elements in a given array of numbers.
    It returns 0 if the array is empty.

    Parameters:
    arr (list): A list of numbers.

    Returns:
    float: The average of all elements in the array.
    """
    return sum(arr) / len(arr) if len(arr) > 0 else 0