"""
QUESTION:
Implement a function `validate_user_registration` that takes seven parameters: `name`, `email`, `phone_number`, `password`, `passport_url`, `is_admin=False`, and `is_politician=False`. 

The function must validate the input data based on the following rules: 
- The `name` should only contain alphabetic characters. 
- The `email` must be a valid email address. 
- The `phone_number` must be at least 10 characters long.
- The `passport_url` must be a valid URL. 
- The `password` is a required field but has no specific validation rules. 
- The `is_admin` and `is_politician` fields are boolean with default values of `False` and do not need to be validated.

The function should return a dictionary containing any validation errors encountered.
"""

import re

def validate_user_registration(name, email, phone_number, password, passport_url, is_admin=False, is_politician=False):
    errors = {}

    if not name.isalpha():
        errors['name'] = "Person name cannot contain number(s)."

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors['email'] = "Invalid email address."

    if len(phone_number) < 10:
        errors['phone_number'] = f"{phone_number} is not a valid phone number."

    if not re.match(r"https?://\S+", passport_url):
        errors['passport_url'] = "Invalid passport URL."

    if not password:
        errors['password'] = "Password is a required field."

    return errors