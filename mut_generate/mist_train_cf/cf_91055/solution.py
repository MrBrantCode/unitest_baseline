"""
QUESTION:
Create a function `filter_positive_numbers` that takes a list of integers as input and returns a new sorted list containing only the positive numbers greater than 10. The resulting list should be sorted in ascending order.
"""

def filter_positive_numbers(nums):
    """
    This function takes a list of integers as input, filters out the positive numbers greater than 10, 
    and returns them in a new sorted list in ascending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A sorted list of positive integers greater than 10.
    """
    return sorted([num for num in nums if num > 10 and num > 0])