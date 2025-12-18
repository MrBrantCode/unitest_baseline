"""
QUESTION:
Write a function named `extract_country_code` that takes a string phone_number as input. The function should extract and return the two-digit country code from the given phone number if it is in the format "+cc xxx-xxx-xxxx" where cc is the country code and xxx-xxx-xxxx has exactly 10 digits. If the input string does not match the specified format, the function should return None.
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