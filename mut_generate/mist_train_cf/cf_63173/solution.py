"""
QUESTION:
Create a function called `email_check` that takes a string representing an email address and returns 'Valid' if the email address is legitimate and 'Invalid' otherwise. The function must be case-sensitive and enforce the following conditions:

- The email address must not begin or end with a period '.'.
- It must contain only a single '@' symbol, which must be surrounded by characters ('a'-'z', 'A'-'Z') on both sides.
- The substring between the '@' symbol and the dot must contain at least two characters.
- The substring after the '.' must be one of the following: ['com', 'org', 'edu', 'net'].
- The length of the email address (including the '@' symbol) must be within the range of 5 and 50 characters.
"""

import re

def email_check(email):
    if 5 <= len(email) <= 50: 
        if re.match(r"^[a-zA-Z]+[a-zA-Z0-9]*@[a-zA-Z]{2,}\.(com|org|edu|net)$", email):
            return 'Valid'
    return 'Invalid'