"""
QUESTION:
Design a function `parse_passport_info` that takes a string as input and returns a dictionary containing the country of issue, passport number, and expiry date. The input string is semi-colon-separated and is expected to be in the format "Country;PassportNumber;YYYY-MM-DD". The function should return "Not a valid string." if the input string does not match the expected format.
"""

import re

def parse_passport_info(string):
    regex = r"([A-Za-z0-9_-]*);([A-Za-z0-9_-]*);([0-9]{4}-[0-9]{2}-[0-9]{2})"
    match = re.match(regex, string)
    if match:
        return {"country": match.group(1),
                "passport_number": match.group(2),
                "expiry_date": match.group(3)}
    else:
        return "Not a valid string."