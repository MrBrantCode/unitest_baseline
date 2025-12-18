"""
QUESTION:
Write a function named LCS that takes two strings X and Y as input and returns the length of the longest common subsequence between them. The function should use dynamic programming to build a 2D array storing the lengths of common subsequences found so far. The function should not return the actual subsequence, just the length of the longest one.
"""

def LCS(X , Y): 
    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n + 1) for i in range(m + 1)] 

    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    return L[m][n]