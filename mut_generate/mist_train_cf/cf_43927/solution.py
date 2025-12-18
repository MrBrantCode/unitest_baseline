"""
QUESTION:
Create a function `longest_common_subsequence(x, y)` that finds the length of the longest common subsequence of two sequences `x` and `y`. The sequences are not required to occupy consecutive positions within the original sequences.
"""

def longest_common_subsequence(x, y):
    m = len(x)
    n = len(y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    return L[m][n]