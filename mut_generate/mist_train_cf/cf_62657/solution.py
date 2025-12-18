"""
QUESTION:
Write a function named `match_string` that takes a string `s` as input and returns `True` if the string matches the following pattern, and `False` otherwise. The pattern should match strings that start with 'abc', followed by a 3-digit number, and optionally followed by a mix of 2 uppercase alphabets and 2 lowercase alphabets in any order. The pattern should also recognize the string 'abc123' as a valid match.
"""

import re

def match_string(s):
  pattern = r"^abc\d{3}(?:(?:[a-z]{2}[A-Z]{2})|(?:[A-Z]{2}[a-z]{2}))?$"
  return bool(re.match(pattern, s))