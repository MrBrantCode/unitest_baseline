"""
QUESTION:
Write a function named `is_valid_email` that takes one string argument, returns a boolean value, and uses regular expressions to determine if the input string represents a valid email address.
"""

import re

def is_valid_email(email):
    """
    This function checks if the input string is a valid email address using regular expressions.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    # Define the regular expression pattern for a valid email address
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Use the fullmatch function to check if the email matches the pattern
    # fullmatch ensures that the entire string matches the pattern, not just a part of it
    if re.fullmatch(pattern, email):
        return True
    else:
        return False