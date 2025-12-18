"""
QUESTION:
Write a function `validate_email` that takes an email address as input and returns `True` if it is valid according to the rules specified in the RFC5322 document, and `False` otherwise. The function should check for the presence of exactly one '@' symbol, valid characters before and after '@', and at least one '.' after '@'. Note that a full implementation of RFC5322 is complex and may require a full-fledged parser or a third-party library.
"""

import re

def validate_email(email):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    return bool(email_regex.match(email))