"""
QUESTION:
Create a function called `extract_country_code` that takes a string representing a phone number as input. The phone number is in the format +cc xxx-xxx-xxxx, where cc is a two-digit country code. The function should return the country code if the input is in the correct format; otherwise, it should return None.
"""

import re

def extract_country_code(phone_number):
    # Define the pattern to match the country code
    pattern = r'\+(\d{2}) \d{3}-\d{3}-\d{4}'
    
    # Use regex to find the country code
    match = re.match(pattern, phone_number)
    
    if match:
        country_code = match.group(1)
        return country_code
    else:
        return None