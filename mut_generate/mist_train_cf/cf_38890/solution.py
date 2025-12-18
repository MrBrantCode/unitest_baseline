"""
QUESTION:
Write a function or class method named `validate_registration_form` that takes three string parameters: `student_id`, `password`, and `confirmation`. The function should validate `student_id`, `password`, and `confirmation` based on the following rules:
- `student_id` should start with "PB" followed by exactly 8 digits (0-9).
- `password` and `confirmation` should only contain alphanumeric characters (a-z, A-Z, 0-9).
- `password` and `confirmation` should match each other.
The function should return three boolean values indicating whether `student_id`, `password`, and `confirmation` are valid or not.
"""

import re

def validate_registration_form(student_id, password, confirmation):
    # Validate student ID: Should start with "PB" followed by exactly 8 digits (0-9)
    is_student_id_valid = bool(re.match(r'^PB[0-9]{8}$', student_id))

    # Validate password: Should only contain alphanumeric characters (a-z, A-Z, 0-9)
    is_password_valid = bool(re.match(r'^[a-zA-Z0-9]+$', password))

    # Validate confirmation: Confirm password matches the original password
    is_confirmation_valid = password == confirmation

    return is_student_id_valid, is_password_valid, is_confirmation_valid