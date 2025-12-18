"""
QUESTION:
You are given two arrays: `keys` of distinct keys and `freq` of their corresponding frequencies. Construct an optimal binary search tree using these keys such that the total search cost is minimized, where the search cost for a key is the depth of the key multiplied by its frequency. Write a function `minSearchCost` that takes these two arrays as input and returns the minimum total search cost. 

The function `minSearchCost(keys, freq)` should take two parameters:
1. An array `keys` of n distinct keys.
2. An array `freq` of length n, where `freq[i]` represents the frequency of occurrence of the ith key.

The function should return the minimum total search cost required to construct an optimal binary search tree using the given keys and their frequencies. 

Constraints: 1 <= n <= 100, where n is the number of keys, and 1 <= keys[i], freq[i] <= 100.
"""

def minSearchCost(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for r in range(i, j + 1):
                c = dp[i][r - 1] if r > i else 0
                c += dp[r + 1][j] if r < j else 0
                c += sum(freq[i:j + 1])
                if c < dp[i][j]:
                    dp[i][j] = c

    return dp[0][n - 1]