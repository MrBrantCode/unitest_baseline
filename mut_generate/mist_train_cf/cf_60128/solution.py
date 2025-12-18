"""
QUESTION:
Write a function `solve(s1, s2)` that takes two input strings `s1` and `s2` and returns a list of all unique longest common substrings present in both strings. If there are multiple unique longest common substrings, return them in alphabetical order. The function should be able to handle overlapping matching substrings in the original strings.
"""

def solve(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0
    end = 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end = i
    lcs = set()
    for i in range(m - length + 1):
        if s1[i:i + length] in s2:
            lcs.add(s1[i:i + length])
    return sorted(list(lcs))