"""
QUESTION:
Write a function `canPartition(arr)` that takes an integer array `arr` as input and returns `True` if it is possible to divide the array into two non-empty subsets `S1` and `S2` such that the sum of elements in `S1` is equal to the sum of elements in `S2`, and `False` otherwise. The array `arr` has a length between 2 and 30, and each element in `arr` is between 0 and 10^4.
"""

def canPartition(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in arr:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[-1]