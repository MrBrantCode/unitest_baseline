"""
QUESTION:
Write a Python function `find_strings_with_char` that takes two parameters: a list of strings and a single character. The function should return a new list containing only the strings from the original list where the specified character appears.
"""

def find_strings_with_char(lst, char):
  result = [word for word in lst if char in word]
  return result