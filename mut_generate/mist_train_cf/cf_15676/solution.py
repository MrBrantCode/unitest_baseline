"""
QUESTION:
Write a function `validate_user_input` that takes in a dictionary with 'name', 'email', and 'phone_number' as keys. Validate the input for each field according to the following rules: 

- 'name' should be at least 3 characters long and should not contain any special characters or numbers.
- 'email' should be a valid email address format (e.g. john.doe@example.com).
- 'phone_number' should be a valid phone number format and should include the country code (e.g. +1 123-456-7890).

The function should return a boolean indicating whether the input is valid and a list of error messages if the input is not valid. The function should not throw any exceptions.
"""

import re

def validate_user_input(user_input):
    """
    Validate user input for 'name', 'email', and 'phone_number'.

    Args:
    user_input (dict): A dictionary containing 'name', 'email', and 'phone_number'.

    Returns:
    tuple: A boolean indicating whether the input is valid and a list of error messages if the input is not valid.
    """
    errors = []
    is_valid = True

    # Validate name
    if not re.match('^[a-zA-Z ]{3,}$', user_input.get('name', '')):
        errors.append("Name should be at least 3 characters long and should not contain any special characters or numbers.")
        is_valid = False

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', user_input.get('email', '')):
        errors.append("Email should be a valid email address format.")
        is_valid = False

    # Validate phone number
    if not re.match(r'^\+[0-9]{1,3} [0-9]{3}-[0-9]{3}-[0-9]{4}$', user_input.get('phone_number', '')):
        errors.append("Phone number should be a valid phone number format and should include the country code.")
        is_valid = False

    return is_valid, errors