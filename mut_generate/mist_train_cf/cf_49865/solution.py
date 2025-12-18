"""
QUESTION:
Given two strings `str1` and `str2`, write a function `lcs(str1, str2)` to find the length of the longest common subsequence. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. The function should use dynamic programming principles and return the length of the longest common subsequence. The function should be able to handle strings of any length.
"""

def lcs(str1, str2):
  m = len(str1)
  n = len(str2)

  # Create a 2D array to store the length of LCS for each sub-problem
  dp = [[None]*(n+1) for i in range(m+1)]

  # Filling the 2D array in bottom up manner
  for i in range(m+1):
    for j in range(n+1):
      # For the base case, if either string is empty, the LCS length is 0
      if i == 0 or j == 0 :
        dp[i][j] = 0
      # If the current characters match, add 1 to the LCS length of the sub-problem without current characters
      elif str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1]+1
      # If the current characters don't match, the LCS length is the maximum of the sub-problems without the current character in str1 or str2
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  # return the LCS length of the original problem
  return dp[m][n]