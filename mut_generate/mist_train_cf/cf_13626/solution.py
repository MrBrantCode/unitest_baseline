"""
QUESTION:
Write a function `sum_even_numbers` that calculates the sum of even numbers in a given array of integers with a length of at least 10. The function should use a single loop to iterate through the array and return the sum of the even numbers.
"""

def sum_even_numbers(arr):
    """
    Calculate the sum of even numbers in a given array of integers.

    Args:
        arr (list): A list of integers with a length of at least 10.

    Returns:
        int: The sum of the even numbers in the array.
    """
    total_sum = 0
    for num in arr:
        if num % 2 == 0:
            total_sum += num
    return total_sum