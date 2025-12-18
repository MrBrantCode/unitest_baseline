"""
QUESTION:
Create a function `validateFields` that takes five parameters: `name`, `address`, `phone`, `email`, and `age`. The function should validate each field based on the following rules: 

- `name` should only contain alphabetical characters and spaces, have a maximum length of 50 characters, and not contain any special characters or numbers.
- `address` should only contain alphanumeric characters, spaces, commas, periods, and have a maximum length of 100 characters.
- `phone` should only contain numeric characters, have a minimum length of 10 digits, and not contain any special characters or letters.
- `email` should be a valid email address following the format "username@domain.com".
- `age` should contain numeric characters and be within the range of 18 to 100.

The function should return `True` if all the values are valid and `False` otherwise.
"""

import re

def validateFields(name, address, phone, email, age):
    if not re.match(r'^[a-zA-Z ]{1,50}$', name):
        return False
    
    if not re.match(r'^[a-zA-Z0-9,. ]{1,100}$', address):
        return False
    
    if not re.match(r'^[0-9]{10,}$', phone):
        return False
    
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return False
    
    if not re.match(r'^[0-9]{2,3}$', age) or not (18 <= int(age) <= 100):
        return False
    
    return True