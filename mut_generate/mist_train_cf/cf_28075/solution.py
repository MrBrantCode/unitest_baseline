"""
QUESTION:
Given two strings S and T of lengths m and n (1 <= m, n <= 1000), write a function `longestCommonSubsequence(S, T)` that returns the length of the longest common subsequence between S and T. The function should use memoization to optimize the computation, where '*' in string S can match any character in string T. The function `lcs(i, j)` calculates the length of the longest common subsequence between the prefix of S ending at index i and the prefix of T ending at index j, and it should be defined within `longestCommonSubsequence(S, T)`.
"""

def longestCommonSubsequence(S, T):
    m, n = len(S), len(T)
    LCS = [[0] * (n + 1) for _ in range(m + 1)]

    def lcs(i, j):
        if i < 0 or j < 0:
            return 0
        if LCS[i][j] > 0:
            return LCS[i][j]
        if S[i-1] != '*':
            if S[i-1] == T[j-1]:
                LCS[i][j] = max(LCS[i][j], lcs(i-1, j-1) + 1)
            else:
                LCS[i][j] = max(LCS[i][j], lcs(i-1, j), lcs(i, j-1))
        else:
            LCS[i][j] = max(LCS[i][j], max(lcs(i-1, j), lcs(i, j-1)))
        return LCS[i][j]

    return lcs(m, n)