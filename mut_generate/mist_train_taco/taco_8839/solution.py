"""
QUESTION:
Your users passwords were all stole in the Yahoo! hack, and it turns out they have been lax in creating secure passwords.  Create a function that checks their new password (passed as a string) to make sure it meets the following requirements:


Between 8 - 20 characters

Contains only the following characters: (and at least one character from each category): uppercase letters, lowercase letters, digits, and the special characters !@#$%^&*?




Return "valid" if passed or else "not valid"
"""

import re

def validate_password(password: str) -> str:
    """
    Validates a password based on the following criteria:
    - Between 8 and 20 characters.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
    - Contains at least one special character from the set: !@#$%^&*?

    Parameters:
    - password (str): The password to be validated.

    Returns:
    - str: "valid" if the password meets all the criteria, otherwise "not valid".
    """
    if re.search(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', password):
        return 'valid'
    else:
        return 'not valid'