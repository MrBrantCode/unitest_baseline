"""
QUESTION:
Create a function called `validate_registration_info` that takes in three parameters: `username`, `email`, and `password`. The function should return `True` if the provided information is valid for registration, and `False` otherwise.

The username should be unique and alphanumeric, with a minimum length of 6 characters. The email address should be in a valid format (e.g. email@example.com) and should be unique. The password should meet the following criteria: at least 10 characters long, contains at least one uppercase letter, contains at least one lowercase letter, contains at least one digit, and contains at least one special character (!@#$%^&*).
"""

import re

def validate_registration_info(username, email, password):
    """
    Validate registration information.

    Args:
    username (str): The username for registration.
    email (str): The email address for registration.
    password (str): The password for registration.

    Returns:
    bool: True if the provided information is valid for registration, False otherwise.
    """

    # Check if username is alphanumeric and at least 6 characters long
    if not re.match("^[a-zA-Z0-9]{6,}$", username):
        return False

    # Check if email is in a valid format
    if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False

    # Check if password meets the required criteria
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$", password):
        return False

    # If all checks pass, return True
    return True