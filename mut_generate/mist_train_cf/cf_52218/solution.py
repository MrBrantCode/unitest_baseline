"""
QUESTION:
Given an array of unique binary strings `strs` and two integers `m` and `n`, find the size of the largest subset of `strs` that contains at most `m` zeros and `n` ones. 

Function name: `findMaxForm(strs, m, n)`

Restrictions: 
- 1 <= len(strs) <= 600 
- 1 <= len(strs[i]) <= 100 
- strs[i] consists only of digits '0' and '1'
- 1 <= m, n <= 100
"""

def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        zeros, ones = s.count('0'), s.count('1')
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    return dp[m][n]