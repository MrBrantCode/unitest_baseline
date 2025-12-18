"""
QUESTION:
Given three binary strings b1, b2, and b3 of lengths m, n, and o respectively, write a function lcs(b1, b2, b3, m, n, o) to find the length of the longest common contiguous series that occurs in all three strings. The function should have a time complexity of O(n^2), where m, n, o <= n.
"""

def lcs(b1, b2, b3, m, n, o): 
    dp = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]
    result = 0 
  
    for i in range(m+1): 
        for j in range(n+1): 
            for k in range(o+1): 
                if (i == 0 or j == 0 or k == 0): 
                    dp[i][j][k] = 0
                elif (b1[i-1] == b2[j-1] and b1[i-1] == b3[k-1]): 
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    result = max(result, dp[i][j][k]) 
                else: 
                    dp[i][j][k] = 0
    return result 