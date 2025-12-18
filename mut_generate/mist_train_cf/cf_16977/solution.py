"""
QUESTION:
Create a function called `extract_information` that takes a string as input in the format "Lastname, Firstname - Age - Address", where the address is in the format "Street, City, State, Country". The function should return a dictionary with the keys 'first_name', 'last_name', 'age', and 'address' containing the extracted information. The function should validate that the age is a positive integer and the address is in a valid format. If the input string is not in the correct format or the age or address is invalid, the function should return `None`.
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
    if age <= 0 or not re.match(r'^.*,.*, \w+,\s\w+$', address):
        return None
    
    # Create and return the dictionary
    return {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'address': address
    }