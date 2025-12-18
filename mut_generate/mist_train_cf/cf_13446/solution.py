"""
QUESTION:
Create a function validateForm to validate a login form with two input fields (username and password) according to the following rules:

- The username field only accepts alphanumeric characters.
- The password field must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one special character.

Return false if the input is invalid and display an error message, otherwise return true.
"""

import re

def validateForm(username, password):
    """
    Validates a login form with two input fields (username and password).

    Args:
    username (str): The username to validate.
    password (str): The password to validate.

    Returns:
    bool: True if the input is valid, False otherwise.
    """
    
    # Check if the username contains only alphanumeric characters
    if not re.match("^[0-9a-zA-Z]+$", username):
        print("Username must contain only alphanumeric characters")
        return False

    # Check if the password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one special character
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    if not password_pattern.match(password):
        print("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
        return False

    return True