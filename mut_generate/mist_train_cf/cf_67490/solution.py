"""
QUESTION:
Given two non-empty strings X and Y, write a function `lcs(X, Y)` to find the length of the longest common subsequence between X and Y. The function should return an integer value representing the length of the longest common subsequence. Note that the input strings may contain alphabetic or numeric characters and the subsequence should be a contiguous sequence of characters.
"""

def lcs(X, Y): 
    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n+1) for i in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
    return L[m][n]