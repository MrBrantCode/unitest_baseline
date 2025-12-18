"""
QUESTION:
Write a function `smallest_subset_sum(nums, K)` that takes a list of distinct integers `nums` and an integer `K` as input and returns the sum of the smallest subset of `nums` that adds up to exactly `K`. Each number in `nums` can only be used once in the subset. If there is no subset of `nums` that adds up to exactly `K`, return -1.
"""

def smallest_subset_sum(nums, K):
    n = len(nums)
    dp = [[False] * (K+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, K+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    if not dp[n][K]:
        return -1
    subset = []
    i, j = n, K
    while i > 0 and j > 0:
        if dp[i-1][j]:
            i -= 1
        else:
            subset.append(nums[i-1])
            j -= nums[i-1]
            i -= 1
    return sum(subset)