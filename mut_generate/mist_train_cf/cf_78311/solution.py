"""
QUESTION:
Given two character sequences s1 and s2, write a function `longest_common_subsequence(s1, s2)` to find and return the most extensive identical subsequence shared by them. The function should take two parameters: s1 and s2, both strings, and return a string representing the longest common subsequence.
"""

def longest_common_subsequence(s1, s2):
  m = len(s1)
  n = len(s2)

  dp = [[0]*(n+1) for i in range(m+1)]

  for i in range(m+1):
    for j in range(n+1):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  i, j = m, n
  lcs = ""
  while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
      lcs = s1[i-1] + lcs
      i -= 1
      j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
      i -= 1
    else:
      j -= 1

  return lcs