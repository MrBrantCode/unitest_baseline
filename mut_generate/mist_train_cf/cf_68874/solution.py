"""
QUESTION:
Write a function named `sum_odd_numbers` that takes an array of integers as input and returns the sum of all odd numbers in the array. The function should have a time complexity of O(n), where n is the length of the array.
"""

def sum_odd_numbers(arr):
    """
    This function calculates the sum of all odd numbers in a given array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The sum of all odd numbers in the array.
    """
    return sum(num for num in arr if num % 2 != 0)