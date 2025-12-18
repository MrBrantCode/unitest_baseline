"""
QUESTION:
Implement a function `isMatch` in the `Solution` class that takes two strings `s` and `p` as input and returns a boolean indicating whether the string `s` matches the pattern `p`. The pattern `p` can contain '*' and '.' where '*' represents any sequence of characters (including an empty sequence) and '.' matches any single character. 

Restrictions: 
- The function should use dynamic programming to solve the problem. 
- The function should return True if the string `s` matches the pattern `p`, False otherwise.
"""

def isMatch(s: str, p: str) -> bool:
    """
    We define the state dp[i][j] to be true if s[0..i) matches p[0..j) and false otherwise. 
    Then the state equations will be as follows:

    p[j - 1] != '*' : dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1] or p[j - 1] == '.'.
    p[j - 1] == '*' : dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.').
    """
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and p[j] in {s[i], '.'}
            if j + 1 < len(p) and p[j + 1] == '*':
                dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
            else:
                dp[i][j] = match and dp[i+1][j+1]

    return dp[0][0]