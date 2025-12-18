"""
QUESTION:
Create a function `longest_common_string(str1, str2, str3)` that takes three strings as input and returns the length of the longest common substring among the three input strings.
"""

def longest_common_string(str1, str2, str3):
    n1, n2, n3 = len(str1), len(str2), len(str3)
    dp = [[[0 for _ in range(n3+1)] for _ in range(n2+1)] for _ in range(n1+1)]
    
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if str1[i-1] == str2[j-1] == str3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[n1][n2][n3]