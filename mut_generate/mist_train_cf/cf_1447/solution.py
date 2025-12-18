"""
QUESTION:
Write a function `find_combinations(nums, target)` that returns the number of distinct combinations of the given positive integers in `nums` that sum up to the `target`. You may reuse the elements of `nums` and assume that each input would have exactly one solution. The solution should have a time complexity of O(n * target), where n is the length of `nums`. The length of `nums` will not exceed 100 and the maximum value of `target` will not exceed 1000.
"""

def find_combinations(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]

    return dp[target]