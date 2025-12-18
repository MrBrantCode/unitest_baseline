"""
QUESTION:
Write a function called max_subarray_sum that takes an array of integers as input and returns the maximum sum of a subarray that meets the following conditions: the subarray is non-empty, contiguous, and has a length of 3 or more. If no such subarray exists, return the maximum sum of any non-empty contiguous subarray.
"""

def max_subarray_sum(nums):
    if len(nums) < 3:
        return max_sum_subarray(nums)
    
    max_sum = float('-inf')
    current_sum = float('-inf')
    for i in range(len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
        else:
            current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            
    # Consider subarray of length 3 or more
    subarray_sum = float('-inf')
    for i in range(len(nums)):
        subarray_sum = nums[i]
        for j in range(i + 1, len(nums)):
            subarray_sum += nums[j]
            if j - i + 1 >= 3 and subarray_sum > max_sum:
                max_sum = subarray_sum
    return max_sum

def max_sum_subarray(nums):
    max_sum = float('-inf')
    current_sum = float('-inf')
    for num in nums:
        if current_sum < 0:
            current_sum = num
        else:
            current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum