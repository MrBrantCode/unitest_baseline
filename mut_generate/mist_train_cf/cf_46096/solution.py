"""
QUESTION:
Write a function `find_numbers_in_text(text)` that uses regular expressions to detect and isolate every numerical value embedded within the provided text, including integers, decimals, and numbers in scientific notation. The function should return a list of the extracted numerical values as strings.
"""

import re

def find_numbers_in_text(text):
  pattern = r'[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'
  matches = re.findall(pattern, text)
  return matches