"""
QUESTION:
Write a function named `validate_password` to determine if a given password is valid. The password is valid if it meets the following conditions: 
- its length is between 10 and 16 characters (inclusive), 
- it contains at least one uppercase character, one lowercase character, one digit, and one special character, 
- it does not contain any spaces, 
- and it does not contain any repeating characters consecutively (e.g., "aa" or "11").
"""

def validate_password(password):
    """
    Validates a password based on the following conditions:
    - its length is between 10 and 16 characters (inclusive),
    - it contains at least one uppercase character, one lowercase character, one digit, and one special character,
    - it does not contain any spaces,
    - and it does not contain any repeating characters consecutively.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # Check if the password length is within the valid range
    if not 10 <= len(password) <= 16:
        return False

    # Check if the password contains at least one uppercase character, one lowercase character, one digit, and one special character
    if not (any(char.isupper() for char in password) and 
            any(char.islower() for char in password) and 
            any(char.isdigit() for char in password) and 
            any(not char.isalnum() for char in password)):
        return False

    # Check if the password contains any spaces
    if ' ' in password:
        return False

    # Check for repeating characters consecutively
    for i in range(1, len(password)):
        # If the current character is equal to the previous character and is not a special character, return False
        if password[i] == password[i-1] and password[i].isalnum():
            return False

    # If all conditions pass, return True
    return True