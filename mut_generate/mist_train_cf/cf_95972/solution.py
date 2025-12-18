"""
QUESTION:
Create a function called `format_phone_number` that takes a string `phone_number` as input. The function should format the given phone number in the format "(123) 456-7890" and output a string with the canonical format of "+1-123-456-7890". The function should handle cases where the phone number is passed in as a string or with additional characters such as hyphens or dots, and validate that the phone number is a valid US phone number according to the North American Numbering Plan (NANP), which requires a 10-digit number.
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