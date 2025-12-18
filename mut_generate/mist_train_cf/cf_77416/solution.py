"""
QUESTION:
Implement a function `validate_string` that takes a string as input and returns True if it matches the following conditions, False otherwise:

- The string contains only alphabets, numbers, and special characters.
- The special characters should not be the first or last character of the string.
- The string should contain at least one uppercase letter, one lowercase letter, and one digit.
"""

import re

def validate_string(string):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9!@#$%^&*()-_+=;':\",.<>/?[\]{}|`~]*$"
    return bool(re.match(pattern, string))