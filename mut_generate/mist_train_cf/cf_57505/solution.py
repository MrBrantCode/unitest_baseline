"""
QUESTION:
Write a function `replace_character` that takes three parameters: a string and two characters, `char1` and `char2`. The function should return a new string with all occurrences of `char1` replaced by `char2`. The function should have a time complexity of O(n), where n is the length of the string.
"""

def replace_character(string, char1, char2):
  new_string = ""
  for char in string:
    if char == char1:
      new_string += char2
    else:
      new_string += char
  return new_string