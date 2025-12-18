"""
QUESTION:
Write a function `longest_common_subsequence(string1, string2)` that finds the length of the longest common subsequence in two input strings `string1` and `string2`. A subsequence is a sequence obtained by deleting some elements from the original sequence, but maintaining the order of the remaining elements. The function should have a time complexity of O(n^2), where n is the length of the longest string in the input, and the maximum length of the input strings will be 1000 characters.
"""

def entance(string1, string2):
    n = len(string1)
    m = len(string2)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]