"""
QUESTION:
Write a function `longestCommonSubsequence(X, Y, Z, m, n, o)` that takes three distinct textual strings `X`, `Y`, `Z` and their lengths `m`, `n`, `o` as input, and returns the length of the lengthiest shared subsequence of characters within them. The function should not use any built-in string comparison or subsequence identification libraries.
"""

def longestCommonSubsequence(X, Y, Z, m, n, o): 
    L = [[[0 for i in range(o+1)]
            for j in range(n+1)]
                for k in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                elif (X[i-1] == Y[j-1] and 
                      X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(max(L[i-1][j][k], 
                                         L[i][j-1][k]),
                                     L[i][j][k-1])
    return L[m][n][o]