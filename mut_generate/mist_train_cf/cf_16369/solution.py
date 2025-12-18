"""
QUESTION:
Create a function `is_valid_email(email)` that takes a string `email` as input and returns `True` if it is a valid email address and `False` otherwise. The function should check if the email address adheres to the following rules:
- The username (before the "@" symbol) is 1-64 characters long and contains only alphanumeric characters, dots, underscores, or hyphens, without consecutive dots, underscores, or hyphens.
- The email address contains the "@" symbol.
- The domain name (after the "@" symbol) is 1-255 characters long, starts with a combination of alphanumeric characters, contains at least one dot, and does not end with a dot or contain consecutive dots or special characters other than dots.
- The email address does not end with a dot.
"""

import re

def is_valid_email(email):
    regex = r"^(?!.*(\.\.|\.\-|\.\_|\_\_|\_\-|\-\_|\-\-))[\w.\-_]{1,64}@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,63}\.){1,}[a-zA-Z]{2,63}$"
    return bool(re.match(regex, email))