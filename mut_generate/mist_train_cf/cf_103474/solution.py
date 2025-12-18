"""
QUESTION:
Write a function named `sum_odd_numbers` that takes an array of integers as input and returns the sum of all the odd numbers in the array. The function should iterate through each element in the array and check if it is odd, adding it to the sum if it is.
"""

def sum_odd_numbers(data):
    """
    This function calculates the sum of all odd numbers in a given array.

    Args:
        data (list): A list of integers.

    Returns:
        int: The sum of all odd numbers in the array.
    """
    sum_odd = 0
    for num in data:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd