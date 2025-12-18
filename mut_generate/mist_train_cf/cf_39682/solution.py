"""
QUESTION:
Create a function `validate_registration_form` that takes an email, phone number, and password as input. The function should validate the input data according to the following rules:
- Email: It should be a valid email address.
- Phone Number: It should be a valid phone number with a country code followed by the number.
- Password: It should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
The function should return a boolean value indicating whether the input data is valid.
"""

import re

def validate_registration_form(email, phone_number, password):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_regex = r'^\+\d{1,3}\d{10,}$'
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    return bool(re.match(email_regex, email) and re.match(phone_regex, phone_number) and re.match(password_regex, password))