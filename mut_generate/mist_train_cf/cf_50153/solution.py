"""
QUESTION:
Create a function named `validate_email` that takes one string argument. Design a regex pattern to match complex email structures, considering the following rules:
- Email can start with alphanumeric characters, '.', or '_'.
- After the initial character, email can contain alphanumeric characters, '.', '_', or '-'.
- Email must contain '@' symbol after the initial characters.
- After '@', domain name follows which can be alphanumeric or contain '-'.
- Domain name is followed by '.' and then one or more alphanumeric characters with possible '.' in between.
- The function should return "Valid Email" if the input string matches the pattern, otherwise return "Invalid Email".
"""

import re

def validate_email(email):
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    pattern = re.compile(regex)
    match = re.search(pattern, email)
    if match != None:
        return "Valid Email"
    else:
        return "Invalid Email"