"""
QUESTION:
Create a function `check_password_strength` that takes a password as input and returns a tuple containing a boolean indicating whether the password is strong and a corresponding message. The function should follow the NIST guidelines, with the following minimum requirements: 
- The password length must be between 10 and 64 characters.
- The password must contain at least one digit.
- The password must contain at least one lowercase letter.
- The password must contain at least one uppercase letter.
- The password must contain at least one special character.
"""

import string

def check_password_strength(password):
    """
    Checks if a password is strong based on the NIST guidelines.

    Args:
    password (str): The password to be checked.

    Returns:
    tuple: A tuple containing a boolean indicating whether the password is strong and a corresponding message.
    """

    min_pwd_length = 10
    max_pwd_length = 64

    if len(password) < min_pwd_length:
        return False, "Password is too short. It should be at least 10 characters long."
    
    if len(password) > max_pwd_length:
        return False, "Password is too long. It should not exceed 64 characters."
    
    if not any(char.isdigit() for char in password):
        return False, "Password should contain at least one digit."

    if not any(char.islower() for char in password):
        return False, "Password should contain at least one lowercase letter."
            
    if not any(char.isupper() for char in password):
        return False, "Password should contain at least one uppercase letter."

    if not any(char in string.punctuation for char in password):
        return False, "Password should contain at least one special character."
    
    return True, "Strong password."