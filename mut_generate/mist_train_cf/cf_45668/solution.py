"""
QUESTION:
Write a function `find_numbers_with_country_code(text)` that takes a string `text` as input and returns a list of valid phone numbers with their respective country codes. Each phone number in the list should be a tuple containing the country code and the phone number without the country code. 

The function should consider phone numbers in various formats, including the use of spaces, hyphens, or brackets in separate sections of the phone number. It should also accommodate different lengths of phone numbers for each country. The country code must be preceded by either a plus (+) sign or a double zero (00). If a phone number without a country code is found, it should not be included in the output list.
"""

import re

def find_numbers_with_country_code(text):
    pattern = r"(\+\d{1,3}|00\d{1,3})[-\s\()]*\d{1,4}[-\s\)]*\d{1,4}[-\s]*\d{1,4}[-\s]*\d{1,4}[-\s]*\d{1,4}"
    matches = re.finditer(pattern, text)
    results = []
    for match in matches:
        raw_number = match.group(0)
        has_country_code = re.match(r"(\+\d{1,3}|00\d{1,3})", raw_number)

        if has_country_code:
            country_code = has_country_code.group(0)
            number = re.sub(r"[^\d]", "", raw_number)
            results.append((country_code, number))

    return results