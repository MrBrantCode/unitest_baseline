"""
QUESTION:
Implement a function `checkPartitioning(s: str) -> bool` that determines if a given string `s` can be split into three non-empty palindromic substrings without any repeating characters. The function should return `true` if possible, and `false` otherwise. The input string `s` consists only of lowercase English letters and has a length between 6 and 2000.
"""

def checkPartitioning(s: str) -> bool:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if length == 1:
                dp[start][end] = True
            elif length == 2:
                dp[start][end] = (s[start] == s[end])
            else:
                dp[start][end] = (s[start] == s[end] and dp[start + 1][end - 1] and len(set(s[start:end+1])) == len(s[start:end+1]))
    dp1 = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j][i - 1]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
    return dp1[-1] >= 3