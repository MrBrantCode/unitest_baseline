"""
QUESTION:
Design a function `validate_email` that accepts an email address as a string and returns `True` if it is a valid email address, and `False` otherwise. The function should use a regular expression pattern to match the input string. The email address is valid if it contains letters, numbers, periods, and underscores, followed by '@', then letters, numbers, periods, and underscores, followed by a period and letters. 

Use the `validate_email` function in a GUI application where users can input their email addresses. When the user submits their email address, the application should display a welcome message if the email is valid, and an error message otherwise.
"""

import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False