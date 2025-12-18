"""
QUESTION:
Create a function named `validate_password` to check if a given password meets the specified criteria. The password must be at least 12 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character.
"""

import re

def validate_password(password):
    """
    Checks if the given password meets the specified criteria.

    The password must be at least 12 characters long and include at least one:
    - Uppercase letter
    - Lowercase letter
    - Number
    - Special character

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    # Define the regular expression patterns for each criteria
    uppercase_pattern = re.compile(r"[A-Z]")
    lowercase_pattern = re.compile(r"[a-z]")
    number_pattern = re.compile(r"\d")
    special_char_pattern = re.compile(r"[^A-Za-z0-9]")

    # Check the password length
    if len(password) < 12:
        return False

    # Check for each criteria
    if (uppercase_pattern.search(password) is None or
            lowercase_pattern.search(password) is None or
            number_pattern.search(password) is None or
            special_char_pattern.search(password) is None):
        return False

    # If all checks pass, the password is valid
    return True