"""
QUESTION:
Write a function `has_common_sequence` that takes three parameters: two strings `str1` and `str2`, and an integer `m`. This function should determine whether there exists a common subsequence of length `m` in `str1` and `str2`. The function should return `True` if such a common subsequence exists and `False` otherwise. The lengths of `str1` and `str2` are represented by `n` and `p` respectively, but these lengths are not necessarily fixed values.
"""

def entance(str1, str2, m):
    n = len(str1) 
    p = len(str2)
    
    # Constructing the L table in the bottom up manner
    L = [[0] * (p+1) for i in range(n+1)]
    
    for i in range(n+1): 
        for j in range(p+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[n][p] >= m