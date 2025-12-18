"""
QUESTION:
Write a function `LCSof3(a, b, c)` that takes three distinct strings `a`, `b`, and `c` as input and returns the length of the longest common subsequence (LCS) of characters among them. The function should work for strings of varying sizes and consider character case (uppercase and lowercase) and punctuation. The function should have a time complexity of O(m*n*p), where `m`, `n`, and `p` are the lengths of `a`, `b`, and `c`, respectively.
"""

def LCSof3(a, b, c):
    n1, n2, n3 = len(a), len(b), len(c)
    
    dp = [[[0 for k in range(n3+1)] for i in range(n2+1)] for j in range(n1+1)]
    
    for i in range(n1+1):
        for j in range(n2+1):
            for k in range(n3+1):
                if (i == 0 or j == 0 or k == 0):
                    dp[i][j][k] = 0
                elif (a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]):
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
   
    return dp[n1][n2][n3]