"""
QUESTION:
Design a function named `max_subarray_sum` that takes in a list of integers and returns the maximum sum that can be obtained by adding a subarray of the given list. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def max_subarray_sum(nums):
    """
    This function returns the maximum sum that can be obtained by adding a subarray of the given list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum sum that can be obtained by adding a subarray.
    """
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum