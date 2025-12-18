"""
QUESTION:
Write a function `min_jumps(nums)` that takes an array of non-negative integers `nums` as input and returns the minimum number of jumps to reach the last index, where each element in the array represents the maximum jump length at that position and you can only jump to indices that are prime numbers. The function should assume that the last index can always be reached. The input array has a length between 1 and 1000, inclusive, and each element in the array is between 0 and 10^5, inclusive.
"""

def min_jumps(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        if is_prime(i):  
            for j in range(i):  
                if j + nums[j] >= i:  
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]