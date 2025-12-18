"""
QUESTION:
Write a function named 'sum_between_10_and_20' that calculates the total of numbers in a given array that are greater than 10 and less than 20. The input array is a list of integers.
"""

def sum_between_10_and_20(arr):
    """
    This function calculates the total of numbers in a given array that are greater than 10 and less than 20.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The total of numbers in the array that are greater than 10 and less than 20.
    """
    return sum(num for num in arr if 10 < num < 20)