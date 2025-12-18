"""
QUESTION:
Extract the country code from a given phone number string. The country code can have a maximum of 3 digits and may be preceded by a '+' sign or enclosed in parentheses, with possible variations in spacing and hyphens. The function should handle phone numbers in the formats +cc (xxx) xxx-xxx-xxxx, (xx)-xxx-xxx-xxxx, +cc xxxxxxxxxx, and cxxxxxxxxxx. Create a function named `extract_country_code` that takes a string `phone_number` as input and returns the extracted country code as a string.
"""

import re

def extract_country_code(phone_number):
    pattern = r'[\+|\(]?(\d{1,3})[\)]?' 
    match = re.search(pattern, phone_number)
    if match:
        return match.group(1)
    else:
        return None