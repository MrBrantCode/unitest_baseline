"""
QUESTION:
Write a function `count_divisible_by_three` that takes a list of integers as input and returns the frequency of numbers that are divisible by 3 and numbers that are not divisible by 3 within the list.
"""

def count_divisible_by_three(nums):
    """
    This function calculates the frequency of numbers that are divisible by 3 
    and numbers that are not divisible by 3 within the given list.

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing the frequency of numbers divisible by 3 and not divisible by 3.
    """
    divisible_by_3 = sum(1 for num in nums if num % 3 == 0)
    not_divisible_by_3 = len(nums) - divisible_by_3
    return divisible_by_3, not_divisible_by_3