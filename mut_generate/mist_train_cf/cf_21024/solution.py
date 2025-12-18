"""
QUESTION:
Write a function `find_first_odd_greater_than_10` that takes a list of positive integers as input and returns the first odd number in the list that is greater than 10. If no such number exists, the function should return None.
"""

def find_first_odd_greater_than_10(nums):
    """
    This function takes a list of positive integers as input and returns 
    the first odd number in the list that is greater than 10. If no such 
    number exists, the function returns None.

    Args:
        nums (list): A list of positive integers.

    Returns:
        int or None: The first odd number greater than 10, or None if not found.
    """
    for num in nums:
        if num > 10 and num % 2 != 0:
            return num
    return None