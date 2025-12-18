"""
QUESTION:
Write a function `sum_even_numbers` that calculates the sum of all even numbers in a given array, excluding negative numbers and numbers divisible by 3.
"""

def sum_even_numbers(nums):
    """
    This function calculates the sum of all even numbers in a given array, 
    excluding negative numbers and numbers divisible by 3.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the array, excluding negative numbers and numbers divisible by 3.
    """
    return sum(num for num in nums if num > 0 and num % 2 == 0 and num % 3 != 0)