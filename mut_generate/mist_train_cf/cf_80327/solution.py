"""
QUESTION:
Write a function `longest_common_subsequence(s1, s2)` that takes two sequences of whole numbers `s1` and `s2` as input parameters. The function should return the longest strictly ascending subsequence that is common to both sequences. The subsequence should be a list of numbers in ascending order.
"""

def longest_common_subsequence(s1, s2):
  m, n = len(s1), len(s2)
  dp = [[0] * (n+1) for _ in range(m+1)]

  for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
      if s1[i] == s2[j]:
        dp[i][j] = 1 + dp[i+1][j+1]
      else:
        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
  
  i, j = 0, 0
  common = []

  while i < m and j < n:
    if s1[i] == s2[j]:
      if not common or s1[i] > common[-1]:
        common.append(s1[i])
      i += 1
      j += 1
    elif dp[i+1][j] > dp[i][j+1]:
      i += 1
    else:
      j += 1

  return common