"""
QUESTION:
Create a function `validate_registration` that takes in user input for name, email, and phone number. The function should validate the input for each field according to the following criteria:
- Name should be at least 3 characters long and should not contain any special characters or numbers.
- Email should be a valid email address format (e.g. john.doe@example.com).
- Phone number should be a valid phone number format and should include the country code (e.g. +1 123-456-7890).
The function should also check if the email and phone number are unique and not already registered by another user. The function should return a dictionary with a boolean 'is_valid' and a list of error messages.
"""

import re

def validate_registration(name, email, phone_number, registered_emails=None, registered_numbers=None):
    """
    Validate user registration input.

    Args:
    name (str): The user's name.
    email (str): The user's email.
    phone_number (str): The user's phone number.
    registered_emails (list, optional): A list of already registered emails. Defaults to None.
    registered_numbers (list, optional): A list of already registered phone numbers. Defaults to None.

    Returns:
    dict: A dictionary with a boolean 'is_valid' and a list of error messages.
    """
    
    # Initialize error messages list and is_valid flag
    error_messages = []
    is_valid = True

    # Check if name is at least 3 characters long and does not contain special characters or numbers
    if not re.match("^[a-zA-Z ]+$", name) or len(name) < 3:
        error_messages.append("Name should be at least 3 characters long and should not contain any special characters or numbers.")
        is_valid = False

    # Check if email is a valid email address format
    if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        error_messages.append("Email should be a valid email address format.")
        is_valid = False

    # Check if email is unique
    if registered_emails and email in registered_emails:
        error_messages.append("Email is already registered by another user.")
        is_valid = False

    # Check if phone number is a valid phone number format
    if not re.match("^\+[0-9]{1,3} [0-9]{3}-[0-9]{3}-[0-9]{4}$", phone_number):
        error_messages.append("Phone number should be a valid phone number format and should include the country code.")
        is_valid = False

    # Check if phone number is unique
    if registered_numbers and phone_number in registered_numbers:
        error_messages.append("Phone number is already registered by another user.")
        is_valid = False

    # Return the validation result
    return {"is_valid": is_valid, "error_messages": error_messages}