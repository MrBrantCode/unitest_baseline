"""
QUESTION:
Implement the `validate_input` method for the `InputValidator` class, which should take a dictionary of user inputs as an argument. The method should validate the inputs using regular expressions, sanitize the inputs by stripping whitespace and converting email addresses to lowercase, and return a tuple containing the sanitized input dictionary and a boolean indicating whether the input was valid or not. The method should also generate detailed error logs and classify errors by type. 

The regular expressions should enforce the following rules: 
- The 'name' field should contain only letters and spaces, with a maximum length of 50 characters.
- The 'email' field should match the standard email format.
- The 'password' field should contain at least one letter and one digit, with a minimum length of 8 characters.

The method should also handle cases where the input dictionary contains fields other than 'name', 'email', and 'password', and sanitize these fields by stripping whitespace.
"""

import re
from typing import Dict, Tuple

def validate_input(input_dict: Dict[str, str]) -> Tuple[Dict[str, str], bool]:
    """
    Validates and sanitizes user input for a RESTful API.

    :param input_dict: A dictionary containing user inputs.
    :return: A tuple containing a sanitized input dictionary and a boolean indicating
    whether the input was valid or not.
    """
    # Define regular expressions for input validation
    name_regex = re.compile(r"^[A-Za-z\s]{1,50}$")
    email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password_regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")

    # Define the sanitized input dictionary
    sanitized_input = {}

    # Validate and sanitize each input field
    error_logs = []
    for field, value in input_dict.items():
        if field == 'name':
            if not name_regex.match(value):
                error_logs.append({'type': 'name', 'message': 'Invalid name.'})
                return sanitized_input, False
            sanitized_input[field] = value.strip()
        elif field == 'email':
            if not email_regex.match(value):
                error_logs.append({'type': 'email', 'message': 'Invalid email.'})
                return sanitized_input, False
            sanitized_input[field] = value.lower().strip()
        elif field == 'password':
            if not password_regex.match(value):
                error_logs.append({'type': 'password', 'message': 'Invalid password.'})
                return sanitized_input, False
            sanitized_input[field] = value.strip()
        else:
            sanitized_input[field] = value.strip()

    # Return the sanitized input dictionary and indicate that the input was valid
    return sanitized_input, len(error_logs) == 0