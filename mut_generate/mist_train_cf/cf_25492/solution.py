"""
QUESTION:
Write a function `find_longest_substring(s)` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The function should only consider non-overlapping substrings and should not include any repeating characters.
"""

def find_longest_substring(s):
  """
  Returns the length of the longest substring without repeating characters.

  Args:
    s (str): The input string.

  Returns:
    int: The length of the longest substring without repeating characters.
  """
  max_length = 0
  start = 0
  usedChar = {}

  for i in range(len(s)):
    if s[i] in usedChar and start <= usedChar[s[i]]:
        start = usedChar[s[i]] + 1
    else:
        max_length = max(max_length, i - start + 1)

    usedChar[s[i]] = i

  return max_length