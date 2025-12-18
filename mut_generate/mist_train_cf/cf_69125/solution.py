"""
QUESTION:
Create a function `alpha_uppercase(word)` that takes a string `word` as input and returns `True` if the word consists solely of uppercase English alphabetic elements and has at least 8 characters, and `False` otherwise.
"""

import re

def alpha_uppercase(word):
  pattern = re.compile('^[A-Z]{8,}$')
  if pattern.match(word):
    return True
  else:
    return False