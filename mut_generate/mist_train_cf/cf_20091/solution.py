"""
QUESTION:
Create a function named `format_phone_number` that takes a phone number as input and returns a string representing the phone number in the format "+1-XXX-XXX-XXXX". The function must remove any non-digit characters from the input phone number, validate that the resulting phone number is a 10-digit number according to the North American Numbering Plan (NANP), and return an error message "Invalid phone number" if the phone number is not valid.
"""

import re

def format_phone_number(phone_number):
    # Remove all non-digit characters from the phone number
    phone_number = re.sub(r'\D', '', phone_number)
    
    # Check if the phone number is valid according to NANP
    if len(phone_number) != 10:
        return "Invalid phone number"
    
    # Format the phone number
    formatted_number = "+1-{}-{}-{}".format(phone_number[:3], phone_number[3:6], phone_number[6:])
    return formatted_number