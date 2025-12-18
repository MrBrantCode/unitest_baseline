"""
QUESTION:
Write a function named `lcsOf3` that takes three strings `X`, `Y`, and `Z` and their lengths `m`, `n`, and `p` as input, and returns the length of the longest common subsequence among the three strings. The function should consider case-sensitivity and special characters. The solution should also be space-optimized and include an optimization to reduce the pre-processing time for larger strings. The function should not include any redundant or irrelevant information and should directly solve the problem at hand.
"""

def lcsOf3(X, Y, Z, m, n, p):
    L = [[[0 for i in range(p+1)] for j in range(n+1)] for k in range(m+1)]
 
    # Building L[m+1][n+1][p+1] in bottom-up fashion
    for i in range(m+1):
        for j in range(n+1):
            for k in range(p+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(max(L[i-1][j][k], L[i][j-1][k]), L[i][j][k-1])
    return L[m][n][p]