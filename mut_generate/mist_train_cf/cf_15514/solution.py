"""
QUESTION:
Write a function called `validate_input` that takes two parameters: `username` and `password`. The function should return `True` if both the username and password meet the requirements and `False` otherwise.

Requirements:
1. The username must be at least 6 characters long and contain only lowercase letters.
2. The password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g. !@#$%^&*).
3. The username and password must not be the same.
4. The password must not contain the username as a substring.

The function should also provide error messages if the input does not meet the requirements.
"""

def validate_input(username, password):
    """
    Validates a username and password based on specific requirements.

    Args:
    username (str): The username to validate.
    password (str): The password to validate.

    Returns:
    bool: True if the username and password are valid, False otherwise.
    """
    # Check if username is at least 6 characters long and contains only lowercase letters
    if len(username) < 6 or not username.islower():
        print("Username must be at least 6 characters long and contain only lowercase letters.")
        return False

    # Check if password is at least 8 characters long and meets the required criteria
    if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or not any(char in "!@#$%^&*" for char in password):
        print("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return False

    # Check if username and password are the same
    if username == password:
        print("Username and password cannot be the same.")
        return False

    # Check if password contains the username as a substring
    if username in password:
        print("Password must not contain the username as a substring.")
        return False

    return True