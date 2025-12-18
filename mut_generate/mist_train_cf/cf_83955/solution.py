"""
QUESTION:
Write a function `maxSubArray` that takes an array of integers as input and returns the maximum sum that can be achieved from all unique subarray combinations. The function should handle empty arrays and arrays with negative numbers.
"""

def maxSubArray(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum