"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that finds the longest common substring between two input strings `s1` and `s2`. The function should return the longest common substring. Note that the longest common substring is not necessarily unique, but any one of them will do.
"""

def longest_common_substring(s1, s2): 
    m = len(s1)
    n = len(s2)
    # Matrix to store lengths of longest common suffixes.
    LCSuff = [[0 for x in range(n+1)] for y in range(m+1)]
    longest_length = 0
    ending_index = 0
  
    # Fill table in bottom-up manner.
    for i in range(1, m+1): 
        for j in range(1, n+1): 
            if s1[i-1] == s2[j-1]: 
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                if LCSuff[i][j] > longest_length: 
                    longest_length = LCSuff[i][j] 
                    ending_index = i - 1
            else: 
                LCSuff[i][j] = 0
    return s1[ending_index-longest_length+1 : ending_index+1]