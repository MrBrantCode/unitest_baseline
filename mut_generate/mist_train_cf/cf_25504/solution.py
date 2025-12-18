"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns the length of the longest common substring between them. The function should not use any external libraries and should only consider contiguous substrings.
"""

def longest_common_substring(s1, s2): 
    m = len(s1) 
    n = len(s2) 
  
    # initialize matrix 
    L = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    # To store the length of longest common substring 
    length = 0 
  
    # Comparing each character of s1 and s2 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If current character of s1 and s2 matches 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1
                length = max(length, L[i][j]) 
            else: 
                L[i][j] = 0
  
    return length 