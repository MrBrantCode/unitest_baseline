"""
QUESTION:
Create a function named validate_email to match a specific format of email address using regex. The email address should consist of two parts: the username and the domain. The username should only allow lowercase alphabets, digits, and the special characters +, -, _, and .. The domain should consist of lowercase alphabets and digits, separated by a period (.). The username should have a minimum length of 3 characters and a maximum length of 20 characters. The domain should have a minimum length of 2 characters and a maximum length of 10 characters.
"""

import re

def validate_email(email):
    """
    Validate an email address using regex.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-z0-9\+\-\_\.]{3,20}@[a-z0-9]{2,10}\.[a-z0-9]{2,10}$"
    return bool(re.match(pattern, email))