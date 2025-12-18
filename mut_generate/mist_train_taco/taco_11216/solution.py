"""
QUESTION:
## Description
Your job is to create a simple password validation function, as seen on many websites. 

The rules for a valid password are as follows:
- There needs to be at least 1 uppercase letter.
- There needs to be at least 1 lowercase letter.
- There needs to be at least 1 number.
- The password needs to be at least 8 characters long.

You are permitted to use any methods to validate the password.

## Examples:

### Extra info
- You will only be passed strings.
- The string can contain any standard keyboard character.
- Accepted strings can be any length, as long as they are 8 characters or more.
"""

def is_valid_password(password: str) -> bool:
    """
    Validates if the given password meets the following criteria:
    - At least 1 uppercase letter.
    - At least 1 lowercase letter.
    - At least 1 number.
    - At least 8 characters long.

    Parameters:
    - password (str): The password string to be validated.

    Returns:
    - bool: True if the password is valid, otherwise False.
    """
    if len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    return has_upper and has_lower and has_digit