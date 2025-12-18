"""
QUESTION:
Create a function called `validate_email` that takes a string as input and returns True if it matches a specific email address format, and False otherwise. The email address should consist of two parts: the username and the domain. The username should only allow lowercase alphabets, digits, and the special characters +, -, _, and .. The domain should consist of lowercase alphabets and digits, separated by a period (.). The username should have a minimum length of 3 characters and a maximum length of 20 characters. The domain should have a minimum length of 2 characters and a maximum length of 10 characters.
"""

import re

def validate_email(email):
    """
    Validate an email address.

    The email address should consist of two parts: the username and the domain.
    The username should only allow lowercase alphabets, digits, and the special characters +, -, _, and ..
    The domain should consist of lowercase alphabets and digits, separated by a period (.).
    The username should have a minimum length of 3 characters and a maximum length of 20 characters.
    The domain should have a minimum length of 2 characters and a maximum length of 10 characters.

    Parameters:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^(?<![.])[a-z0-9+_.-]{3,20}(?![.])@[a-z0-9]{2,10}\.[a-z0-9]{2,10}$"
    return bool(re.match(pattern, email))