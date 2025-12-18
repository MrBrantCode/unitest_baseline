"""
QUESTION:
Write a function `longest_common_subsequence(X, Y, Z, m, n, p)` that finds the length of the longest common subsequence of three sequences `X`, `Y`, and `Z` with lengths `m`, `n`, and `p` respectively. The function should be able to handle special characters and numerical values, and should have a time complexity better than O(n^3), specifically O(n*m*p).
"""

def longest_common_subsequence(X, Y, Z, m, n, p):
    LCS = [[[0 for k in range(p+1)] for j in range(n+1)]for i in range(m+1)]
 
    # Fill LCS[][][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
            for k in range(p+1):
                if (i == 0 or j == 0 or k == 0):
                    LCS[i][j][k] = 0
                elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]):
                    LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
                else:
                    LCS[i][j][k] = max(max(LCS[i-1][j][k], LCS[i][j-1][k]), LCS[i][j][k-1])
 
    # Return LCS of two sequences
    return LCS[m][n][p]