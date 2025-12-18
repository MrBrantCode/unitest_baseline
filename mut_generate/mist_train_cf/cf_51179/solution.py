"""
QUESTION:
Create a function `validate_email(email)` that checks if the input `email` string adheres to standard email format protocols using regular expressions. The function should return or print whether the email is valid or not, but it does not need to verify the actual existence of the email account. The email format should include one or more alphanumeric characters at the start, followed by an optional period or underscore, then '@', followed by one or more word characters, a period, and finally two or three word characters at the end.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
    return bool(re.search(pattern, email))