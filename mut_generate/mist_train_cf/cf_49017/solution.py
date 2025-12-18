"""
QUESTION:
Write a function `findMaxLength(nums)` that finds the maximum length of a contiguous subarray with equal sum of the first half and the second half in the given array of integers `nums`. The length of the given integer array `nums` will not exceed 50,000.
"""

def findMaxLength(nums):
    max_length = 0
    hashmap = {0: -1}
    prefix_sum = [0] * len(nums)
    prefix_sum_diff = [0] * len(nums)
    
    for i in range(len(nums)):
        if i == 0:
            prefix_sum[i] = nums[i]
        else:
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        prefix_sum_diff[i] = 2 * prefix_sum[i] - (i + 1)

    for j in range(len(prefix_sum_diff)):
        if prefix_sum_diff[j] not in hashmap:
            hashmap[prefix_sum_diff[j]] = j
        else:
            max_length = max(max_length, j - hashmap[prefix_sum_diff[j]])
            
    return max_length