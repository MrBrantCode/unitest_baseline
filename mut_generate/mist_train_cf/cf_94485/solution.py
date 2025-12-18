"""
QUESTION:
Extract the first name, last name, age, and address from a string in the format "Lastname, Firstname - Age - Address" and return a dictionary with the extracted information. The address should be in the format "Street, City, State, Country". The function, `extract_information`, should validate that the age is a positive integer and the address is in a valid format. If the validation fails or the string is in an incorrect format, the function should return `None`.
"""

import re

def extract_information(string):
    # Use regular expressions to extract the information
    pattern = r'^(.*),\s(.*)\s-\s(\d+)\s-\s(.*,\s.*, \w+,\s\w+)$'
    match = re.match(pattern, string)
    
    # If the pattern doesn't match, return None
    if not match:
        return None
    
    # Extract the groups from the match
    last_name = match.group(1)
    first_name = match.group(2)
    age = int(match.group(3))
    address = match.group(4)
    
    # Validate the age and address
    if age <= 0 or not validate_address(address):
        return None
    
    # Create and return the dictionary
    return {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'address': address
    }

def validate_address(address):
    # Use regular expressions to validate the address format
    pattern = r'^.*,.*, \w+,\s\w+$'
    return re.match(pattern, address) is not None