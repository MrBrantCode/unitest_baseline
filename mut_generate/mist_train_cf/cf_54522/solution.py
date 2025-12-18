"""
QUESTION:
Implement a function `longest_common_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns their longest common substring. The function should be able to handle strings of any length and characters. It should also be able to find the longest common substring even if it appears multiple times in the strings.
"""

def longest_common_substring(s1, s2):
  # Initializing the matrix to store the lengths
  lengths = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
  longest, x_longest = 0, 0
  
  # Iterate over the strings
  for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
      if s1[i-1] == s2[j-1]: 
        lengths[i][j] = lengths[i-1][j-1] + 1
        if lengths[i][j] > longest:
          longest = lengths[i][j]
          x_longest = i
      else:
        lengths[i][j] = 0
  
  # Return the longest common substring
  return s1[x_longest - longest: x_longest]