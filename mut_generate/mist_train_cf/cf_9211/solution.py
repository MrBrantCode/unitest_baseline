"""
QUESTION:
Create a function called `validate_input` that takes two parameters: `username` and `password`. The function should return `True` if both the username and password meet the following requirements:

- The username must be at least 6 characters long and contain only lowercase letters.
- The password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.

If any of the requirements are not met, the function should return `False` and provide an error message to guide the user.
"""

def validate_input(username, password):
    """
    Validates a username and password based on specific requirements.

    Args:
    username (str): The username to validate.
    password (str): The password to validate.

    Returns:
    bool: True if both username and password are valid, False otherwise.
    """
    
    # Check username requirements
    if len(username) < 6 or not username.islower():
        print("Username must be at least 6 characters long and contain only lowercase letters.")
        return False
    
    # Check password requirements
    if len(password) < 8:
        print("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special_char = True
    
    if not (has_uppercase and has_lowercase and has_digit and has_special_char):
        print("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return False
    
    return True