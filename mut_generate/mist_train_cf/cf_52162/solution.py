"""
QUESTION:
Design a function `LCS` that takes three distinct textual strings as input and returns the length of their longest common subsequence, its starting index in each string, and the type of subsequence (e.g., palindrome, anagram, simple string, etc.).
"""

def lcs(string1, string2, string3):
  len1, len2, len3 = len(string1), len(string2), len(string3)
  
  # dp[i][j][k] contains length of LCS for string1[0..i-1], string2[0..j-1], string3[0..k-1] 
  dp = [[[0 for _ in range(len3+1)] for _ in range(len2+1)] for _ in range(len1+1)]
  
  # filling dp[][][] table in bottom up manner 
  for i in range(1, len1+1): 
    for j in range(1, len2+1):
      for k in range(1, len3+1): 
        if (string1[i-1] == string2[j-1] == string3[k-1]): 
          dp[i][j][k] = dp[i-1][j-1][k-1] + 1
        else: 
          dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]) 

  # LCS will be at dp[len1][len2][len3] 
  return dp[len1][len2][len3]