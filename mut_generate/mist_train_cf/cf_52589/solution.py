"""
QUESTION:
Write a function `longest_common_subsequence(s1, s2)` that takes two strings `s1` and `s2` as input and returns the longest contiguous substring common to both. The function should return the longest common substring in its entirety, not just its length. There are no restrictions on the characters in the input strings.
"""

def longest_common_subsequence(s1, s2):
  m = len(s1)
  n = len(s2)

  # An (m+1) times (n+1) matrix
  dp = [["" for _ in range(n+1)] for _ in range(m+1)]

  for i in range(m):
    for j in range(n):
      if s1[i] == s2[j]:
        dp[i+1][j+1] = dp[i][j] + s1[i]
      else:
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)

  return dp[-1][-1]