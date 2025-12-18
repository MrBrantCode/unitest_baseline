"""
QUESTION:
Create a function `verify_password` that takes a password string as input and returns `True` if the password is valid, and `False` otherwise. A valid password must meet the following conditions:

- It must contain at least one uppercase letter.
- It must contain at least one lowercase letter.
- It must contain at least one digit.
- It must contain at least one special character.
- It must not contain any consecutive repeating characters.
- It must not contain any palindromic substrings.
- The password should be verified using a single regular expression.
"""

import re

def verify_password(password: str) -> bool:
    """
    Verifies if the given password is valid based on the following conditions:
    - It must contain at least one uppercase letter.
    - It must contain at least one lowercase letter.
    - It must contain at least one digit.
    - It must contain at least one special character.
    - It must not contain any consecutive repeating characters.
    - It must not contain any palindromic substrings.

    Args:
        password (str): The password to be verified.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    pattern = r'^(?!.*(.).*\1)(?!.*(.)(.)\2\3)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-+_!@#$%^&*.,?]).*$'

    # Use re.fullmatch to ensure the entire password matches the pattern
    return bool(re.fullmatch(pattern, password))