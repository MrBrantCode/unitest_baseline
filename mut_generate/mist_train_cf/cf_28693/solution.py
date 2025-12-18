"""
QUESTION:
Implement the function `isMatch(s: str, p: str) -> bool` that takes in two strings `s` and `p`, where `p` can contain wildcard characters `*` and `?`. The wildcard `*` matches zero or more of any character, while the wildcard `?` matches exactly one of any character. Return `True` if the string `s` matches the pattern `p`, and `False` otherwise.
"""

def isMatch(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] in {s[i - 1], '?'}:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[len(s)][len(p)]