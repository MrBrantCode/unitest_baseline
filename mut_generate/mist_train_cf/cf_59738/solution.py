"""
QUESTION:
Create a function `LCS(word1, word2)` that calculates the length of the longest common subsequence between two input strings `word1` and `word2`. The function should return the length of the longest common subsequence. The definition of "near-identicality" is having all characters of one word as a subsequence in the other one.
"""

def LCS(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[0]*(n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]