"""
QUESTION:
Create a function named `check_email` that takes one string argument `email` and returns a boolean value. The function should use a regex pattern to validate the input string according to standard email address specifications. The regex pattern should match strings that start with one or more alphanumeric characters, dots, underscores, plus signs, or hyphens, followed by the '@' symbol, then one or more alphanumeric characters or hyphens, a period, and finally one or more alphanumeric characters, periods, or hyphens.
"""

import re

def check_email(email):
  pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
  match = re.match(pattern, email)
  return bool(match)