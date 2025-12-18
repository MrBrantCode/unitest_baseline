"""
QUESTION:
Design a function validate_password that takes two parameters: username and password. The function should validate the password based on the following rules: the password must be at least 8 characters long, contain at least one number, and contain at least one special character. If the password is valid, return a dictionary with the status "success" and the message "Password is valid". If the password does not meet the requirements, return a dictionary with the status "error" and a message describing the error. If the username is not found, return a dictionary with the status "error" and the message "User not found". Assume that the user exists for the purpose of this problem unless otherwise stated.
"""

import re

def validate_password(username, password):
    """
    Validates a password based on the following rules:
    - The password must be at least 8 characters long.
    - The password must contain at least one number.
    - The password must contain at least one special character.

    Args:
        username (str): The username (not used in this implementation).
        password (str): The password to be validated.

    Returns:
        dict: A dictionary containing the status and message of the validation result.
    """

    # Check if password is at least 8 characters long
    if len(password) < 8:
        return {"status": "error", "message": "Password must be at least 8 characters long."}

    # Check if password contains at least one number
    if not re.search(r"\d", password):
        return {"status": "error", "message": "Password must contain at least one number."}

    # Check if password contains at least one special character
    if not re.search(r"[^A-Za-z0-9]", password):
        return {"status": "error", "message": "Password must contain at least one special character."}

    # If all checks pass, the password is valid
    return {"status": "success", "message": "Password is valid"}