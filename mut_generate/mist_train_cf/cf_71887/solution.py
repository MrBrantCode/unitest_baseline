"""
QUESTION:
Write a function named `count_non_printable` that takes an input string, counts the number of non-printable characters (excluding whitespace characters), and handles Unicode characters.
"""

import unicodedata
import string

def count_non_printable(s):
  return sum(1 for c in s if unicodedata.category(c)[0] != 'C' and c not in string.whitespace)