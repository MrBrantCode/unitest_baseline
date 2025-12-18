"""
QUESTION:
Write a function `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list, with a time complexity of O(n), where n is the length of the input list.
"""

def get_odd_numbers(nums):
    """
    Returns a new list containing only the odd numbers from the input list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of odd integers.
    """
    return [num for num in nums if num % 2 != 0]