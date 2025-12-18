"""
QUESTION:
Write a function `extract_info(text)` that takes a string `text` as input and returns a tuple of three values: the full name, date of birth, and residential address. The input string is expected to be in the format "Full Name; Date of Birth; Residential Address", where the date of birth is in the format dd/mm/yyyy and the residential address is a string. The function should return "Invalid input string" if the input string does not match the expected format.
"""

import re

def extract_info(text):
    # regex for full name
    name_regex = r"([A-Za-z]+[\s]*[A-Za-z]+)"
    
    # regex for date of birth in format dd/mm/yyyy
    dob_regex = r"(\d{2}[/]\d{2}[/]\d{4})"
    
    # regex for address
    address_regex = r"(\d+[\s]+[A-Za-z]+[\s]+[A-Za-z]+[,]+[\s]*[A-Za-z]+)"
    
    # extract full name
    full_name = re.search(name_regex, text)
    
    # extract date of birth
    dob = re.search(dob_regex, text)
    
    # extract address
    address = re.search(address_regex, text)
    
    if full_name and dob and address:
        return full_name.group(0), dob.group(0), address.group(0)
    else:
        return "Invalid input string"