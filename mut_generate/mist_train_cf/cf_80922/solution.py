"""
QUESTION:
Find the last odd number in a list that is not a multiple of 5 and less than 20. The function should consider both positive and negative numbers, as well as zero. The function name is not specified, so for clarity, let's call it `find_last_odd`.

The function `find_last_odd` should take a list of integers as input and return the last odd number that meets the specified conditions.
"""

def find_last_odd(data):
    """
    Find the last odd number in a list that is not a multiple of 5 and less than 20.

    Args:
        data (list): A list of integers.

    Returns:
        int: The last odd number that meets the specified conditions. If no such number exists, returns None.
    """
    for num in reversed(data):
        # Check if number is less than 20, not a multiple of 5 and is odd.
        if num < 20 and num % 2 != 0 and num % 5 != 0:
            return num
    return None