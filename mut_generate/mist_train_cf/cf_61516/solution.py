"""
QUESTION:
Given a list of strings `strs` where each string is of identical length, find the minimum number of columns to delete such that each remaining string is in lexicographic order. The function `minDeletionSize(strs)` should return the smallest possible value of the number of columns to delete. Note that `1 <= len(strs) <= 100` and `1 <= len(strs[i]) <= 100`.
"""

def minDeletionSize(strs):
    W = len(strs[0])
    dp = [1] * W
    for i in range(W-1, -1, -1):
        for j in range(i+1, W):
            if all(row[i] <= row[j] for row in strs):
                dp[i] = max(dp[i], 1 + dp[j])
    return W - max(dp)