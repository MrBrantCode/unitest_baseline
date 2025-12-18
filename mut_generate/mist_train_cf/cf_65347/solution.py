"""
QUESTION:
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2` with the following weighted operations: 
- Insert a character (costs 2 operations)
- Delete a character (costs 1 operation)
- Replace a character (costs 2 operations)
The function should be named `minDistance(word1, word2)`. The constraints are:
- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.
"""

def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j * 2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  
                               dp[i][j - 1] + 2, 
                               dp[i - 1][j - 1] + 2) 
    return dp[m][n]