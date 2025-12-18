"""
QUESTION:
Write a function named `find_max_element_info` that takes an integer array as input. The function should return a tuple containing three elements: the maximum element in the array, the number of times the maximum element occurs in the array, and a list of indices where the maximum element occurs in ascending order.
"""

def find_max_element_info(nums):
    """
    This function finds the maximum element in the given array, 
    the number of times it occurs, and its indices.

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum element, its frequency, and its indices.
    """
    max_element = max(nums)
    max_count = nums.count(max_element)
    max_indices = [i for i, num in enumerate(nums) if num == max_element]
    return max_element, max_count, max_indices