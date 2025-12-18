"""
QUESTION:
Implement a function named `form_validation` that takes a dictionary-like object `form_data` as input. This function should validate the `form_data` based on the following conditions:
- All fields in `form_data` are required, and the password must be 8 characters or more.
- The name and last name in `form_data` must not contain any numbers.
- The email address in `form_data` must match the regular expression pattern `r"[^@]+@[^@]+\.[^@]+"`.

The `form_validation` function should return a list of error messages if any of the conditions are not met. If no errors are found, the function should return an empty list.
"""

import re

def form_validation(form_data):
    errors = []

    if not all(form_data.values()) or len(form_data.get('password', '')) < 8:
        errors.append("All fields are required and password must be 8 or more characters")

    if any(char.isdigit() for field in ['name', 'last_name'] for char in form_data.get(field, '')):
        errors.append("Name and last name must not contain numbers")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", form_data.get('email', '')):
        errors.append("Invalid Email address")

    return errors