"""
QUESTION:
Implement a function `edit_distance` that takes two strings `str1` and `str2` as input and returns the minimum number of operations (insertions, deletions, and substitutions) required to transform `str1` into `str2`. The time complexity of the solution should be O(n^2), where n is the length of the longer string.
"""

def edit_distance(str1: str, str2: str) -> int:
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]