"""
QUESTION:
Find the number of ways to assign `+`, `-`, and `*` symbols to a list of non-negative integers to make the sum of the integers equal to a target value S. The `*` operation has precedence over `+` and `-`, but parentheses cannot be used. The list length will not exceed 20 and the sum of elements will not exceed 1000. Write a function `findTargetSumWays(nums, S)` to solve this problem, where `nums` is the list of integers and `S` is the target sum. The function should return the number of ways to achieve the target sum.
"""

def findTargetSumWays(nums, S):
    memo = {}
    def helper(index, s):
        if index == len(nums):
            return 1 if s == S else 0
        if (index, s) in memo:
            return memo[(index, s)]
        add = helper(index + 1, s + nums[index])
        subtract = helper(index + 1, s - nums[index])
        multiply = helper(index + 1, s * nums[index]) if s != 0 else 0
        memo[(index, s)] = add + subtract + multiply
        return memo[(index, s)]
    return helper(0, 0)