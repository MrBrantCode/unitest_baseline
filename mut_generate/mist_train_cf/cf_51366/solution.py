"""
QUESTION:
Write a function `longestPalSubsequence(seq)` that takes a string `seq` as input and returns the length of the maximum length palindromic subsequence existing within the string. The function should use dynamic programming to solve the problem efficiently.
"""

def longestPalSubsequence(seq):
    n = len(seq)
  
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)]for y in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
    
    # Build the table using bottom up approach.
    # Iterate over length of sequence from 2 to n
    for seq_len in range(2, n+1):
        for i in range(n-seq_len+1):
            j = i+seq_len-1
            if seq[i] == seq[j] and seq_len == 2:
                L[i][j] = 2
            elif seq[i] == seq[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
    return L[0][n-1]