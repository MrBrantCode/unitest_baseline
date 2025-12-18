"""
QUESTION:
Implement the `lcs` function to find the length of the longest common subsequence in two input strings. The function should take four parameters: `str1`, `str2`, `n`, and `m`, where `n` and `m` are the lengths of `str1` and `str2` respectively. The function should return the length of the longest common subsequence.
"""

def lcs(str1, str2, n, m): 
    if n == 0 or m == 0:          
        return 0
  
    elif str1[n-1] == str2[m-1]:   
        return 1 + lcs(str1, str2, n-1, m-1) 
 
    else: 
        return max(lcs(str1, str2, n, m-1),    
                   lcs(str1, str2, n-1, m))