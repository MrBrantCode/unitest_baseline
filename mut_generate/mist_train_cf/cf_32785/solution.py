"""
QUESTION:
Create a registration validation program using the following functions: `validate_name(name)`, `validate_email(email)`, and `validate_password(password)`. 

- `validate_name(name)`: Validate if a name is not empty and contains only alphabetic characters.
- `validate_email(email)`: Validate if an email is in a valid format, containing an "@" symbol and a domain.
- `validate_password(password)`: Validate if a password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, one digit, and one special character.

Implement the validation logic for each input field using these functions.
"""

import re

def registration_validation(name, email, password):
    def validate_name(name):
        return name.isalpha() and len(name) > 0

    def validate_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def validate_password(password):
        return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password)

    return validate_name(name) and validate_email(email) and validate_password(password)