"""
QUESTION:
Create a function named `filter_even_numbers` that takes a list of integers as input, filters out the even numbers that are not divisible by 3, and returns them in descending order. The function should not modify the original input list.
"""

def filter_even_numbers(nums):
    """
    Filters out the even numbers that are not divisible by 3 from a given list of integers and returns them in descending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of even numbers not divisible by 3 in descending order.
    """
    return sorted([num for num in nums if num % 2 == 0 and num % 3 != 0], reverse=True)