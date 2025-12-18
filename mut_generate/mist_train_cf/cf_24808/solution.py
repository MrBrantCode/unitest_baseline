"""
QUESTION:
Write a function called `compare_strings` that takes two strings as input and returns the longer string. The function should take two parameters, `str1` and `str2`, and return a string.
"""

def compare_strings(str1, str2):
  if len(str1) > len(str2):
    return str1
  else:
    return str2