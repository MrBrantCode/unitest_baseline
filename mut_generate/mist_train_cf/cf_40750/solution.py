"""
QUESTION:
Write a function `isMatch(s: str, p: str) -> bool` to determine if the string `s` matches the pattern `p`. The pattern can include special characters `.` and `*`, where `.` matches any single character and `*` matches zero or more of the preceding element. `s` and `p` are non-null and contain only lowercase letters a-z, and `p` can also contain `.` and `*`. The function should return `True` if `s` matches `p`, and `False` otherwise.
"""

def isMatch(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    
    return dp[len(s)][len(p)]