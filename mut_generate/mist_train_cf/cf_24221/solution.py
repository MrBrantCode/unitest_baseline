"""
QUESTION:
Write a function `maxSubArray` that finds the subarray with the largest sum in an integer array. The function should return the start and end indices of the subarray. The input array is a list of integers, and the function should handle negative numbers. The solution should be efficient and run in O(n) time complexity.
"""

def maxSubArray(nums):
    """
    Finds the subarray with the largest sum in an integer array.

    Args:
    nums (list): A list of integers.

    Returns:
    tuple: The start and end indices of the subarray with the largest sum.

    """
    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(len(nums)):
        max_ending_here += nums[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return start, end