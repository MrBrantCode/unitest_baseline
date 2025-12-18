"""
QUESTION:
Write a function maxSubArraySum that calculates the maximum sum of a sub-array within a given array of integers. The function should take an array of integers as input and return the maximum sum of a contiguous sub-array. The input array can contain both positive and negative integers.
"""

def maxSubArraySum(nums):
    """
    Calculate the maximum sum of a sub-array within a given array of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum sum of a contiguous sub-array.
    """
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum