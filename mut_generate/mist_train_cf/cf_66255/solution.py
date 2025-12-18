"""
QUESTION:
Create a function `extract_info(text)` that extracts information from a given text string in English and French, using regular expressions. The function should be able to handle special characters and extract the full name, exact time, date of birth, and residential address, including apartment numbers. The function should return a dictionary with the extracted information. The input text string may contain variations in formatting, and the regular expressions used in the solution should be modifiable to accommodate these variations.
"""

import re

def extract_info(text):
    # Regular expression patterns
    name_pattern = r"^([a-zA-Z]+ [a-zA-Z]+)"
    date_pattern = r"(\d{2}/\d{2}/\d{4})"
    time_pattern = r"(\d+h\d+)"
    address_pattern = r"(?:réside au|résident of) (.*),"

    # Match patterns and extract info
    name_match = re.search(name_pattern, text)
    name = name_match.group(1) if name_match else None

    date_match = re.search(date_pattern, text)
    dob = date_match.group(1) if date_match else None

    time_match = re.search(time_pattern, text)
    time = time_match.group(1) if time_match else None

    address_match = re.search(address_pattern, text)
    address = address_match.group(1) if address_match else None

    # Return dictionary with information
    return {
        'full_name': name,
        'date_of_birth': dob,
        'time': time,
        'residential_address': address
    }