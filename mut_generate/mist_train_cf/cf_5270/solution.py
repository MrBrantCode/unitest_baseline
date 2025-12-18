"""
QUESTION:
Write a function `extract_city_postal_code` that takes a string as input and returns a list of tuples, where each tuple contains a city name and its corresponding postal code. The city name can consist of multiple words, may contain special characters, and must start with a capital letter and end with a lowercase letter. The postal code must be exactly 5 digits long.
"""

import re

def extract_city_postal_code(address):
    """
    Extract city and postal code from a given address string.

    Args:
    address (str): The input address string.

    Returns:
    list[tuple]: A list of tuples containing city names and their corresponding postal codes.
    """
    
    pattern = r'\b[A-Z][A-Za-z,.\'\s]+\b,\s\d{5}\b'
    matches = re.findall(pattern, address)
    
    extracted_info = []
    for match in matches:
        city, postal_code = match.split(", ")
        extracted_info.append((city, postal_code))
        
    return extracted_info