"""
QUESTION:
Write a function named `lcs(str1, str2)` that calculates the length of the longest common subsequence between two input strings `str1` and `str2`. The function should return an integer value representing the length of the longest common subsequence.
"""

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
 
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]