"""
QUESTION:
Given an array of numbers and a target sum, write a function `find_longest_subsequence(nums, target)` to find the longest non-contiguous increasing subsequence with a length greater than 2 and a sum greater than the target sum. The subsequence cannot contain adjacent numbers from the original array.
"""

def find_longest_subsequence(nums, target):
    n = len(nums)
    dp = [1] * n
    sums = list(nums)
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    sums[i] = sums[j] + nums[i]
                elif dp[j] + 1 == dp[i] and sums[j] + nums[i] > sums[i]:
                    sums[i] = sums[j] + nums[i]
    
    max_length = 0
    max_sum = 0
    result = []
    
    for i in range(n):
        if dp[i] > 2 and sums[i] > target:
            if dp[i] > max_length or (dp[i] == max_length and sums[i] > max_sum):
                max_length = dp[i]
                max_sum = sums[i]
                result = []
            
            result.append(nums[i])
    
    return result