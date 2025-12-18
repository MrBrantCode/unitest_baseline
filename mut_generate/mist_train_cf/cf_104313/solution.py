"""
QUESTION:
Create a function called `validate_fields` for a type with fields "name", "address", "phone", "email", and "age". The function should validate the fields according to the following criteria:

- "name": alphabetical characters only, maximum length 50
- "address": alphanumeric characters, spaces, commas, and periods only, maximum length 100
- "phone": numeric characters only, minimum length 10
- "email": valid email address format "username@domain.com"
- "age": numeric, within the range of 18 to 100

The function should return True if all fields are valid, False otherwise.
"""

import re

def validate_fields(name, address, phone, email, age):
    if not isinstance(name, str) or not re.match("^[a-zA-Z]{1,50}$", name):
        return False
    if not isinstance(address, str) or not re.match("^[a-zA-Z0-9\s,.]{1,100}$", address):
        return False
    if not isinstance(phone, str) or not re.match("^\d{10,}$", phone):
        return False
    if not isinstance(email, str) or not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False
    if not isinstance(age, int) or not 18 <= age <= 100:
        return False
    return True