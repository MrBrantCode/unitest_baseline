"""
QUESTION:
Construct a Python function `verifyEmail(email)` that uses regular expressions to verify the format of an email address. The function should return `True` if the email address matches the basic email format and `False` otherwise. The email format should allow for lowercase and uppercase letters, digits, underscores, dots, plus signs, and dashes before the `@` symbol, followed by letters, digits, and dashes for the domain name, a dot, and then letters, digits, dots, and dashes for the extension.
"""

import re

def verifyEmail(email):
    emailRegex = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    if re.fullmatch(emailRegex, email):
        return True
    else:
        return False