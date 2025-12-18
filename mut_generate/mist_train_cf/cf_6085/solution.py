"""
QUESTION:
Create a function `validate_email(email)` that takes an email address as a string and checks if it is valid. The email is valid if it matches the standard email format, has at least one uppercase letter, one lowercase letter, one number, and one special character, and its length is between 8 and 50 characters. Additionally, the email should not contain any consecutive repeating characters or any whitespace characters.
"""

import re

def validate_email(email):
    """
    Validate an email address.
    
    The email is valid if it matches the standard email format, has at least one 
    uppercase letter, one lowercase letter, one number, and one special character, 
    and its length is between 8 and 50 characters. Additionally, the email should 
    not contain any consecutive repeating characters or any whitespace characters.
    
    Parameters:
    email (str): Email address to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """

    # validate email format
    email_regex = r'^[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+(?:\.[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False

    # validate length
    if len(email) < 8 or len(email) > 50:
        return False

    # validate uppercase letter
    if not any(c.isupper() for c in email):
        return False

    # validate lowercase letter
    if not any(c.islower() for c in email):
        return False

    # validate number
    if not any(c.isdigit() for c in email):
        return False

    # validate special character
    if not any(c in "!#$%&'*+-/=?^_`{|}~" for c in email):
        return False

    # validate consecutive repeating characters
    if re.search(r'(.)\1', email):
        return False

    # validate whitespace characters
    if any(c.isspace() for c in email):
        return False

    return True