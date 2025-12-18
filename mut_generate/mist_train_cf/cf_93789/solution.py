"""
QUESTION:
Write a function `find_max_num` that takes a list of integers as input and returns the maximum number in the list, ignoring any negative numbers and numbers that are divisible by 3.
"""

def find_max_num(nums):
    """
    Find the maximum number in a list, ignoring negative numbers and numbers divisible by 3.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The maximum number in the list, or float('-inf') if no number meets the conditions.
    """
    max_num = float('-inf')  # Initialize max_num with a very small value

    for num in nums:
        if num > 0 and num % 3 != 0:  # Ignore negative numbers and numbers divisible by 3
            max_num = max(max_num, num)

    return max_num