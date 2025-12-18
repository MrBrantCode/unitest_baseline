"""
QUESTION:
Implement a function `isMatch(s, p)` that determines whether an input string `s` matches a given pattern `p` where `.` matches any single character, `*` matches zero or more of the preceding element, and `+` matches one or more of the preceding element. The matching should cover the entire input string.

Constraints:
- `0 <= s.length <= 100`
- `0 <= p.length <= 100`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `.`, `*`, and `+`.
- For each appearance of the character `*` or `+`, there will be a previous valid character to match.
"""

def isMatch(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j + 1 < len(p) and (p[j+1] == '*' or p[j+1] == '+'):
                dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
            elif match:
                dp[i][j] = dp[i+1][j+1]
    
    return dp[0][0]