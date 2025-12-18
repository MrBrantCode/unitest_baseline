"""
QUESTION:
Write a function named `check_substring` that takes two strings `str1` and `str2` as input, and returns a boolean value indicating whether `str1` is a substring of `str2` or not. The function should correctly handle cases with multiple and overlapping instances of substrings.
"""

def check_substring(str1, str2):
  for i in range(len(str2)-len(str1)+1):  
    if str2[i:i+len(str1)] == str1:  
      return True
  return False