"""
QUESTION:
Create a function named `password_strength_checker` that evaluates the complexity of a user's chosen password. The function should check the password against the following criteria: 
- Minimum length of 12 characters
- Presence of at least one uppercase letter
- Presence of at least one lowercase letter
- Presence of at least one number
- Presence of at least one special character
- Avoidance of commonly used passwords, stored in a dictionary. 
The function should return `True` if the password meets all the criteria, `False` otherwise.
"""

def password_strength_checker(password):
    """
    Evaluates the complexity of a user's chosen password.
    
    Args:
    password (str): The user's chosen password.
    
    Returns:
    bool: True if the password meets all the complexity criteria, False otherwise.
    """

    # Dictionary of commonly used passwords
    common_passwords = {"password", "qwerty", "123456", "letmein", "dragonball"}

    # Check if the password is at least 12 characters long
    if len(password) < 12:
        return False

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one number
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one special character
    if not any(not char.isalnum() for char in password):
        return False

    # Check if the password is not a commonly used password
    if password.lower() in common_passwords:
        return False

    # If all checks pass, the password is strong
    return True