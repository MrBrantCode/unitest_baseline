"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a subarray with a length of 3 or more.
"""

def max_subarray_sum(nums):
    """
    This function calculates the maximum sum of a subarray with a length of 3 or more.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum sum of a subarray with a length of 3 or more.
    """

    if len(nums) < 3:
        return None

    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        if len(nums) >= 3 and current_sum > max_sum:
            max_sum = current_sum

    return max_sum