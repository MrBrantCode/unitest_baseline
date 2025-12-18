"""
QUESTION:
Create a function named `validate_email` that checks if a given email address has a valid structure and formatting. The function should take a string as input and return a boolean value (True or False) indicating whether the email address is valid or not. The email address is valid if it matches the following pattern: starts with alphanumeric characters, dots, underscores, or dashes, followed by an '@' symbol, then more alphanumeric characters, dots, underscores, or dashes, and finally a dot and at least two to three alphanumeric characters.
"""

import re

def validate_email(email):
  regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
  if(re.search(regex, email)):
    return True
  else:
    return False