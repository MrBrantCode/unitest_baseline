"""
QUESTION:
Implement the `min_edits(s1, s2)` function to find the minimum number of edits (insertions, deletions, or substitutions of a single character) required to transform string `s1` into string `s2`. The function should take two strings `s1` and `s2` as input and return the minimum number of edits required to make them equal. The function should have a time complexity of O(mn), where m and n are the lengths of `s1` and `s2`, respectively.
"""

def min_edits(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0: # If s1 is empty, we can add j characters from s2
                dp[i][j] = j
            elif j == 0: # If s2 is empty, we can add i characters from s1
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]: # If the current characters are equal, no operations needed
                dp[i][j] = dp[i-1][j-1]
            else: # We need to either insert, delete, or substitute a character
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[m][n]