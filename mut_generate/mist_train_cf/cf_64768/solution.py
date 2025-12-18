"""
QUESTION:
Write a function `check_string` that takes an input string and returns `True` if the string starts with a lowercase alphabetical character from 'a' to 'm', ends with an uppercase alphabetical character from 'N' to 'Z', and allows any combination of alphabetical characters (both lowercase and uppercase), numbers, and special characters `@#$%^&+=` in between.
"""

import re

def check_string(input_string):
  pattern = r"^[a-m]([a-zA-Z0-9@#$%^&+=]*[N-Z])$"
  return bool(re.match(pattern, input_string))