"""
QUESTION:
Create a function `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers. The function should have a time complexity of O(n) and must not use any built-in functions or methods such as filter() or any form of iteration other than the list comprehension itself.
"""

def get_odd_numbers(nums):
    """
    Returns a new list containing only the odd numbers from the input list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of odd integers.
    """
    return [x for x in nums if x % 2 != 0]