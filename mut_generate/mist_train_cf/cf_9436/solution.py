"""
QUESTION:
Write a function `longest_increasing_subsequence` that takes an array of numbers as input and returns the longest increasing subsequence with a length greater than 2. The subsequence should be strictly increasing, meaning each number is greater than the previous one.
"""

def longest_increasing_subsequence(nums):
    if len(nums) < 3:
        return []
    
    dp = [[num] for num in nums]
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [nums[i]]
    
    longest_subsequence = max(dp, key=len)
    
    return longest_subsequence if len(longest_subsequence) > 2 else []