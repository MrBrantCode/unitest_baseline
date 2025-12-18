"""
QUESTION:
Create a function `is_match(s)` that takes a string `s` as input and returns `True` if the string exclusively consists of alphabetic characters from "a" to "z", begins with a vowel, and ends with a consonant, and `False` otherwise.
"""

import re

def is_match(s):
  pattern = r"^[aeiou][a-z]*[bcdfghjklmnpqrstvwxyz]$"
  return bool(re.match(pattern, s))