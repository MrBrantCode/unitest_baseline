"""
QUESTION:
Implement a function `isMatch(s, p)` that returns whether the input string `s` matches the given pattern `p`. The pattern `p` can contain lowercase English letters, `.` (matches any single character), and `*` (matches zero or more of the preceding element). The function should match the entire string `s`, not just a part of it. The input string `s` and pattern `p` have the following restrictions: 
0 <= s.length <= 20, 0 <= p.length <= 30, `s` only contains lowercase English letters, and `p` only contains lowercase English letters, `.` and `*`.
"""

def isMatch(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and p[j] in {s[i], '.'}
            if j+1 < len(p) and p[j+1] == '*':
                dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
            else:
                dp[i][j] = match and dp[i+1][j+1]
    return dp[0][0]