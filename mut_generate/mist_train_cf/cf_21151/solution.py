"""
QUESTION:
Create a function `validateForm` that validates a login form with two input fields: `username` and `password`. The `username` field should only accept alphanumeric characters. The `password` field should have a minimum length of 12 characters and contain at least two uppercase letters, two lowercase letters, and two special characters. If the input fields are invalid, display an error message for each field.
"""

import re

def validate_form(username, password):
    """
    Validates a login form with two input fields: username and password.
    
    Args:
        username (str): The username to validate.
        password (str): The password to validate.
    
    Returns:
        dict: A dictionary containing error messages for each field. If the input fields are valid, the dictionary will be empty.
    """
    errors = {}

    # Validate username
    if not re.match("^[a-zA-Z0-9]+$", username):
        errors["username"] = "Username should only contain alphanumeric characters."

    # Validate password
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$", password):
        errors["password"] = "Password should be at least 12 characters long and contain at least two uppercase letters, two lowercase letters, and two special characters."

    return errors