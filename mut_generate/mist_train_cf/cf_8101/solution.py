"""
QUESTION:
Implement a function called `validate_registration` to validate user registration information. The function should take in a dictionary containing the user's name, address, phone number, email address, and password. Validate the input to ensure that all fields are not empty, the phone number is in a valid format, the email address is valid, and the password meets certain complexity requirements (minimum length of 8 characters, containing at least one uppercase letter, one lowercase letter, one digit, and one special character).
"""

import re

def validate_registration(registration_info):
    """
    Validate user registration information.

    Args:
    registration_info (dict): A dictionary containing user's name, address, phone number, email address, and password.

    Returns:
    bool: True if the registration information is valid, False otherwise.
    """
    
    # Check if all fields are not empty
    if not all(registration_info.values()):
        return False
    
    # Validate phone number format
    phone_number = registration_info['phone_number']
    phone_pattern = re.compile(r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$')
    if not phone_pattern.match(phone_number):
        return False
    
    # Validate email address format
    email = registration_info['email']
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_pattern.match(email):
        return False
    
    # Validate password complexity requirements
    password = registration_info['password']
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
    if not password_pattern.match(password):
        return False
    
    return True