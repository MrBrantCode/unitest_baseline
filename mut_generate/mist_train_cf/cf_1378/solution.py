"""
QUESTION:
Create a function `validate_json_data` that takes a JSON string as input and returns `True` if the JSON data is valid and `False` otherwise. The JSON data is valid if it contains the fields "name", "age", "email", "address", and "phone" with the following conditions:

- The "name" field is a non-empty string.
- The "age" field is a positive integer.
- The "email" field is a valid email address.
- The "address" field is a non-empty string.
- The "phone" field is a valid phone number with the format (XXX) XXX-XXXX.

Assume that the input JSON string is a single object with the above fields.
"""

import json
import re

def validate_json_data(json_string):
    try:
        json_data = json.loads(json_string)
        
        name = json_data.get("name")
        age = json_data.get("age")
        email = json_data.get("email")
        address = json_data.get("address")
        phone = json_data.get("phone")
        
        pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        pattern_phone = r'^\(\d{3}\) \d{3}-\d{4}$'
        
        if name and age and isinstance(age, int) and age > 0 and re.match(pattern_email, email) and address and re.match(pattern_phone, phone):
            return True
        else:
            return False
    
    except json.JSONDecodeError:
        return False