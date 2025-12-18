"""
QUESTION:
Write a function named `check_password` that takes two parameters: `username` and `password`. This function should verify if the password meets the following requirements: 
- The password is at least 8 characters long.
- The password contains at least one uppercase letter, one lowercase letter, one numeric digit, and one special character.
- The password does not contain the username in any form or case.

The function should then classify the password strength as "weak", "medium", or "strong" based on the criteria:
- Weak: Password meets only the length requirement.
- Medium: Password meets the length requirement and contains at least one uppercase letter, one lowercase letter, one numeric digit, and one special character, but contains the username in any form or case.
- Strong: Password meets all the requirements mentioned above.
"""

def check_password(username, password):
    """
    This function checks the strength of a password based on certain criteria.

    Parameters:
    username (str): The username of the user.
    password (str): The password of the user.

    Returns:
    str: A string indicating the strength of the password ("weak", "medium", or "strong").
    """

    # Check if password is at least 8 characters long
    if len(password) < 8:
        return None  # or raise an exception

    # Check if password contains at least one uppercase letter, one lowercase letter, one numeric digit, and one special character
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(not char.isalnum() for char in password)

    # Check if password contains the username in any form or case
    contains_username = username.casefold() in password.casefold()

    # Classify password strength
    if has_uppercase and has_lowercase and has_digit and has_special_char and not contains_username:
        return "strong"
    elif has_uppercase and has_lowercase and has_digit and has_special_char:
        return "medium"
    else:
        return "weak"