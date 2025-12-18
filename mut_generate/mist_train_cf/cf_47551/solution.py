"""
QUESTION:
Write a function `countPalindromicSubsequences(S, K)` that takes a string `S` and an integer `K` as input, and returns the number of different non-empty palindromic subsequences of length `K` in `S`, modulo `10^9 + 7`. 

Restrictions: The length of `S` will be in the range `[1, 1000]`, each character `S[i]` will be in the set `{'a', 'b', 'c', 'd'}`, and the value of `K` will be in the range `[1, length of S]`.
"""

def countPalindromicSubsequences(S: str, K: int) -> int:
  mod = 10**9 + 7
  alphabet_size = 4
  str_length = len(S)
  
  # Convert S into the list of integers
  S = [ord(c) - ord('a') for c in S]
  
  # Create next and prev arrays
  cur = [0]*alphabet_size
  prev = [0]*alphabet_size
  next_letter = [cur[:] for _  in range(str_length)]
  for i in reversed(range(str_length)):
    cur[S[i]] = i + 1
    next_letter[i] = cur[:]
    
  # Create dp array
  dp = [[0]*(str_length + 1) for _ in range(K + 1)]
  for i in range(str_length + 1):
    dp[0][i] = 1
    
  # Fill dp array
  for k in range(1, K + 1):
    for i in range(str_length - k + 1):
      dp[k][i] = dp[k][i+1]
      for x in range(alphabet_size):
        j = next_letter[i][x]
        if j != 0:
          if j == i + 1:
            dp[k][i] += 1
          elif j > i + 1:
            dp[k][i] += dp[k-1][j] + dp[k-1][i+1] - dp[k-1][j-1]
      dp[k][i] %= mod
  return dp[K][0]