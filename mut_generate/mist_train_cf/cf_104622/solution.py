"""
QUESTION:
Create a function named `validate_phone_number` that takes a string representing a phone number as input and returns True if the phone number is valid (10 digits without special characters) and False otherwise.

Use regular expressions to validate the phone number. 

Restrictions: The function should use a regular expression pattern to check for exactly 10 digits.
"""

import re

# Define regular expression pattern for phone number validation
phone_pattern = r'^\d{10}$'

# Function to validate phone number
def validate_phone_number(phone):
    if re.match(phone_pattern, phone):
        return True
    else:
        return False