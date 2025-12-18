"""
QUESTION:
Write a function named `max_sum` that takes a sorted list of integers as input and returns the maximum sum that can be obtained by adding two numbers from the list. The function should have a time complexity less than O(n^2), where n is the number of elements in the list.
"""

def max_sum(nums):
    """
    Calculate the maximum sum of two numbers from a sorted list of integers.

    Args:
        nums (list): A sorted list of integers.

    Returns:
        int: The maximum sum of two numbers from the list.
    """
    return max(nums[-1] + nums[-2], nums[0] + nums[1])