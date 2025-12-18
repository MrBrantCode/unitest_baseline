"""
QUESTION:
Design a function named `password_check` that verifies a password based on the following conditions:

- The password must contain a mix of uppercase letters, lowercase letters, digits, and special characters, excluding spaces and underscores.
- The password must contain at least one non-alphanumeric character that is neither an underscore nor a whitespace.
- No character should be repeated more than twice consecutively.
- The password length must be between 12 and 18 characters.
"""

import re

def password_check(password):
    # At least one uppercase, one lowercase, one digit, one special character
    if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s_])", password):
        return "Password needs to have at least one uppercase, one lowercase, one digit, and one special character."
    
    # No more than two consecutive repeats of the same character
    if re.search(r"(.)\1\1", password):
        return "Password cannot have more than two consecutive repeats of the same character."

    # Length between 12 and 18
    if not 12 <= len(password) <= 18:
        return "Password length must be between 12 and 18."

    # No whitespace
    if " " in password:
        return "Password must not contain spaces."
        
    return "Password is accepted."