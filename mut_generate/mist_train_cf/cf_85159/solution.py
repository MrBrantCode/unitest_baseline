"""
QUESTION:
Develop a function `LCS(X, Y)` that finds the longest common subsequence between two input strings `X` and `Y`. The function should return a string representing the longest common subsequence. The strings `X` and `Y` only contain uppercase English letters.
"""

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
 
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    L = [[0 for j in range(n+1)] for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # Initialize LCS as an empty string
    lcs = ""
    
    # Start from the right-most-bottom-most corner and
    # find one character of LCS in each step.
    i = m
    j = n
    while i > 0 and j > 0:
 
        # If current character in X and Y are same,
        # then current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs = X[i-1] + lcs
            i-=1
            j-=1
            
        # If not same, then find the larger of two and
        # move in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
 
    return lcs