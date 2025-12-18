"""
QUESTION:
Write a function named `find_three_consecutive_nonrepeating_digits` that takes a string `s` as input and returns the first occurrence of three consecutive non-repeating digits in the string. The function should return "No match found" if no such sequence exists.
"""

import re

def find_three_consecutive_nonrepeating_digits(s):
  regex = r"(\d)(?!\1)(\d)(?!\1|\2)(\d)"
  match = re.search(regex, s)
  if match:
    return match.group(0)
  else:
    return "No match found"