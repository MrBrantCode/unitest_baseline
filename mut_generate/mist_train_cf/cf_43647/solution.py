"""
QUESTION:
Write a function `longest_common_subsequence(X, Y, Z, m, n, p)` that returns the length of the longest common subsequence of three sequences `X`, `Y`, and `Z`, where `m`, `n`, and `p` are the lengths of `X`, `Y`, and `Z`, respectively. The function should fill a 3D table `LCStable` in a bottom-up manner to store the lengths of common subsequences. The function should return the length of the longest common subsequence of the three sequences.
"""

def longest_common_subsequence(X, Y, Z, m, n, p):
    LCStable = [[[0 for k in range(p+1)] for j in range(n+1)] for i in range(m+1)]
    
    # Fill LCS table in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
            for k in range(p+1):
                if (i == 0 or j == 0 or k == 0):
                    LCStable[i][j][k] = 0
                elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]):
                    LCStable[i][j][k] = LCStable[i-1][j-1][k-1] + 1
                else:
                    LCStable[i][j][k] = max(max(LCStable[i-1][j][k], LCStable[i][j-1][k]), LCStable[i][j][k-1])
                    
    # Returns length of LCS for three sequences
    return LCStable[m][n][p]