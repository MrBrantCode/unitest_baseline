"""
QUESTION:
Write a function `longest_increasing_subsequence` that takes an array of numbers `nums` and a target sum `target` as input. The function should return the sum of the longest increasing subsequence in `nums` that has a sum greater than `target` and a length greater than 2. If no such subsequence exists, return the maximum sum found.
"""

def longest_increasing_subsequence(nums, target):
    n = len(nums)
    lengths = [1] * n
    sums = nums.copy()

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    sums[i] = sums[j] + nums[i]

    max_length = max(lengths)
    max_sum = float('-inf')

    for i in range(n):
        if lengths[i] == max_length and sums[i] > target and lengths[i] > 2:
            max_sum = max(max_sum, sums[i])
            
    if max_sum == float('-inf'):
        return max(sums)
    else:
        return max_sum