"""
QUESTION:
Create a function called validate_user_input that takes in a dictionary containing user information (name, email, phone number, and password) as input. The function should return True if the input is valid and False otherwise. The validation criteria for each field are:
- Name should be at least 3 characters long and should not contain any special characters or numbers.
- Email should be a valid email address format.
- Phone number should be a valid phone number format and should include the country code.
"""

import re

def validate_user_input(user_info):
    """
    Validate user input based on given criteria.

    Args:
    user_info (dict): A dictionary containing user information.
                      It should have 'name', 'email', 'phone_number', and 'password' keys.

    Returns:
    bool: True if the input is valid, False otherwise.
    """

    # Check if all required fields are present
    required_fields = ['name', 'email', 'phone_number', 'password']
    if not all(field in user_info for field in required_fields):
        return False

    # Validate name
    if not re.match('^[a-zA-Z ]+$', user_info['name']) or len(user_info['name']) < 3:
        return False

    # Validate email
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, user_info['email']):
        return False

    # Validate phone number
    phone_pattern = r'^\+[0-9]{1,3}[- ]?[0-9]{3}[- ]?[0-9]{3}[- ]?[0-9]{4}$'
    if not re.match(phone_pattern, user_info['phone_number']):
        return False

    # If all validation passes, return True
    return True