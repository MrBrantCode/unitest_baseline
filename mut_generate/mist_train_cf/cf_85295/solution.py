"""
QUESTION:
Given an integer `num`, write a function `countingBits` that returns an array of the number of `1`'s in the binary representation of every number in the range `[0, num]` and the sum of all the 1's. The function should have a time complexity of `O(n)`, space complexity of `O(n)`, and should not use any built-in functions for counting bits.
"""

def countingBits(num):
    dp = [0] * (num+1)
    sum = 0
    for i in range(1, num+1):
        dp[i] = dp[i >> 1] + (i & 1)
        sum += dp[i]
    return dp, sum