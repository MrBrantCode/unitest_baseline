"""
QUESTION:
Write a function `isInterleave(s1, s2, s3)` that determines if string `s3` can be formed by interleaving the characters of strings `s1` and `s2` in a way that maintains the left-to-right order of characters from each string. The function should take three string parameters and return a boolean value indicating whether `s3` is an interleaved string of `s1` and `s2`. The function must ensure that the total length of `s1` and `s2` is equal to the length of `s3`.
"""

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0:
                dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            if j > 0:
                dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

    return dp[len(s1)][len(s2)]