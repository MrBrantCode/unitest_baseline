"""
QUESTION:
Write a function `longest_common_prefix` that takes an array of up to 105 strings, each of up to 100 characters, and returns the longest common prefix among all strings in the array. The comparison should be case-sensitive. If the array is empty, return an empty string.
"""

def longest_common_prefix(strings):
  if not strings:
    return ""
  
  shortest = min(strings, key=len)
  for i, char in enumerate(shortest):
    for others in strings:
      if others[i] != char:
        return shortest[:i]
  return shortest