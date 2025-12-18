"""
QUESTION:
Create a function `is_voucher` that checks if a given string is a voucher. A voucher is defined as a string consisting of 4 groups of 4 letters each, separated by a hyphen (-), with no extra characters at the beginning or end of the string. The function should return `True` if the string is a voucher and `False` otherwise.
"""

import re

def is_voucher(s):
  pattern = r'^[A-Za-z]{4}-[A-Za-z]{4}-[A-Za-z]{4}-[A-Za-z]{4}$'
  return bool(re.match(pattern, s))