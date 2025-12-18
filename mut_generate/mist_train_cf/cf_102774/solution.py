"""
QUESTION:
Write a function `sum_divisible_by_three` that takes a list of integers as input and returns the sum of the elements that are divisible by 3.
"""

def sum_divisible_by_three(nums):
    """
    This function calculates the sum of elements in a list that are divisible by 3.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of elements divisible by 3.
    """
    return sum(num for num in nums if num % 3 == 0)