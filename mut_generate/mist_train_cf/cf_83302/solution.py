"""
QUESTION:
Develop a function `postal_code_check(city, postal_code)` that takes a city name and a postal code as input and returns a boolean value indicating whether the postal code matches the city's known format, along with a corresponding message. The function should categorize the postal code into 'Standard Format', 'Large User Format', or 'Business and Government Offices Format' and verify it against a dictionary of valid UK cities and their corresponding postal code formats. 

The function should use regular expressions to match the postal codes against the following patterns:
- Standard Format: A1 1AA
- Large User Format: A1 1AAA
- Business and Government Offices Format: A99 AA

The function should also check if the postal code does not match the city's known format and flag it for review.
"""

import re

# Dictionary of UK cities with their corresponding postal code formats
UK_postal_formats = {'London': 'Standard Format', 'Birmingham': 'Large User Format', 'Edinburgh': 'Business and Government Offices Format'}

def postal_code_check(city, postal_code):
    patterns = {
        'Standard Format': r'^[A-Z]\d \d[A-Z]{2}$',
        'Large User Format': r'^[A-Z]\d \d[A-Z]{3}$',
        'Business and Government Offices Format': r'^[A-Z]\d{1,2} [A-Z]{2}$'
    }

    postal_format = UK_postal_formats[city]
    pattern = patterns[postal_format]

    match = re.match(pattern, postal_code)

    if match is None:
        return False, 'Incorrect Postcode Format. This postal code did not match the city\'s known format. Please review.'
    else:
        return True, 'Correct Postcode Format. This postal code matches the city\'s known format.'