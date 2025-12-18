"""
QUESTION:
Construct a function named `find_street_names` that takes an address string as input and returns a list of street names found in the address. The function should be able to match common street terms such as 'Street', 'Lane', 'Road', 'Boulevard', 'Avenue', and 'Drive', with or without abbreviations and in any case.
"""

import re

def find_street_names(address):
    street_terms = r"(Street|St|Lane|Ln|Road|Rd|Boulevard|Blvd|Avenue|Ave|Drive|Dr)"
    pattern = re.compile(street_terms, re.IGNORECASE)
    matches = re.findall(pattern, address)
    return matches