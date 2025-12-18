"""
QUESTION:
Create a function `password_strength_validator` that takes a username and a password as input and returns the strength of the password as "weak", "medium", or "strong" based on the following criteria:

- The password must be at least 10 characters long.
- The password must contain at least two uppercase letters, two lowercase letters, two numeric digits, and two special characters.
- The password must not contain the user's name in any form or case.
- The password must not contain any whitespace characters.

The function should be case-sensitive when checking for the user's name in the password and should handle edge cases such as an empty password or a password that only consists of a single character type. 

Password strength is classified as follows:
- Weak: Password meets only the length requirement.
- Medium: Password meets the length requirement and contains at least two uppercase letters, two lowercase letters, two numeric digits, and two special characters.
- Strong: Password meets all the requirements mentioned above.
"""

import re

def password_strength_validator(username, password):
    """
    This function validates the strength of a password based on certain criteria.

    Args:
    username (str): The username of the user.
    password (str): The password to be validated.

    Returns:
    str: The strength of the password ("weak", "medium", or "strong").
    """
    
    # Check if the password is at least 10 characters long
    if len(password) < 10:
        return "weak"

    # Check if the password contains the user's name in any form or case
    if username.lower() in password.lower():
        return "weak"

    # Check for whitespace characters in the password
    if any(char.isspace() for char in password):
        return "weak"

    # Initialize counters for uppercase letters, lowercase letters, digits, and special characters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_char_count = 0

    # Count the occurrences of each character type
    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isalnum():
            special_char_count += 1

    # Check if the password meets the criteria for a medium or strong password
    if (uppercase_count >= 2 and lowercase_count >= 2 and digit_count >= 2 and special_char_count >= 2):
        return "strong"
    elif (uppercase_count >= 1 or lowercase_count >= 1 or digit_count >= 1 or special_char_count >= 1):
        return "medium"

    # If none of the above conditions are met, return "weak"
    return "weak"