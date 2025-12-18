"""
QUESTION:
Create a function `validate_email(email)` that uses regex to validate a given email address. The email must end with a top-level domain of .com, .net, or .edu, and must not contain consecutive special characters (. _ -). The function should return True for a valid email and False otherwise.
"""

import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|net|edu)$'
    consecutive_special_characters = r'[\.\-_]{2,}'
    
    if not re.match(pattern, email):
        return False

    if re.search(consecutive_special_characters, email):
        return False

    return True