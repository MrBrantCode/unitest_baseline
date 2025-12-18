"""
QUESTION:
Write a function named `minimumEditDistance(str1, str2)` that computes the minimum edit distance (number of operations to transform one string into another) between two input strings `str1` and `str2` of the same length. The allowed operations are insertion, deletion, and substitution of characters. The function should return the minimum number of operations required to transform `str1` into `str2`. Assume that the input strings are not empty and are of equal length.
"""

def minimumEditDistance(str1, str2):
    m = len(str1)
    n = len(str2)
 
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0: 
                dp[i][j] = j 
            elif j == 0: 
                dp[i][j] = i 
            elif str1[i - 1] == str2[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j - 1],       
                                   dp[i - 1][j],       
                                   dp[i - 1][j - 1]     
                                   ) 
  
    return dp[m][n]