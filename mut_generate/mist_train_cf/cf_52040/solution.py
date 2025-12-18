"""
QUESTION:
Create a function `extract_phone_numbers_and_area_codes` that takes a string `text` as input. The function should use regular expressions to match all occurrences of phone numbers in the formats (999) 999-9999, 999-999-9999, 999.999.9999, and 999 999 9999 within the input text. The function should then extract the area code (the first three digits) from each matched phone number and return a list of the full phone numbers along with a list of their corresponding area codes.
"""

import re

def extract_phone_numbers_and_area_codes(text):
    pattern = re.compile(r'\(?\b\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b')
    phone_numbers = pattern.findall(text)
    
    area_codes = [re.search(r'\d{3}', pn).group(0) for pn in phone_numbers]
    return phone_numbers, area_codes