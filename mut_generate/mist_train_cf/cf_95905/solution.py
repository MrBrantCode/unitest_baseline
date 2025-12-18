"""
QUESTION:
Extract city names and their respective 5-digit postal codes from a string where city names can be multiple words and may contain special characters. The string contains the city names and postal code in the format 'city, state, postal code'. Write a regular expression to extract this information.
"""

import re

def extract_city_postal_code(input_string):
    """
    Extract city names and their respective 5-digit postal codes from a string.

    Args:
        input_string (str): The input string containing city names and postal codes.

    Returns:
        list: A list of tuples containing the city name and postal code.
    """
    regex = r"City:\s*(.+?),\s*Postal Code:\s*(\d{5})"
    matches = re.findall(regex, input_string)

    result = []
    for match in matches:
        city = match[0]
        postal_code = match[1]
        result.append((city, postal_code))
    
    return result