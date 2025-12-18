"""
QUESTION:
Write a function `extract_city_postal_code` that takes a string as input and returns the city names and their respective postal codes. The city names can consist of multiple words and may contain special characters. The postal codes must be exactly 5 digits long. Note that the city name always precedes its postal code and is separated by a comma. The function should extract all city and postal code pairs from the input string.
"""

import re

def extract_city_postal_code(input_string):
    regex = r"City:\s*(.+?),\s*Postal Code:\s*(\d{5})"
    matches = re.findall(regex, input_string)
    return [(match[0], match[1]) for match in matches]