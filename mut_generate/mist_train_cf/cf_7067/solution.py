"""
QUESTION:
Write a function named maxSubArray that finds the maximum contiguous subarray of an integer array and returns its sum along with the starting and ending indices of the subarray. The function should handle edge cases where the array is empty, contains only negative numbers, or has multiple subarrays with the same maximum sum. The function must have a time complexity of O(n) and should not use any extra space.
"""

def maxSubArray(nums):
    if not nums:
        return []

    max_sum = current_sum = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return [max_sum, start, end]