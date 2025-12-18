"""
QUESTION:
Write a function `extract_road_names` that takes an address string as input and returns a list of matches for common road types (Street, St, Rd, Road, Avenue, Ave, Drive, Dr), regardless of case.
"""

import re

def extract_road_names(address):
    pattern = re.compile(r'\b(Street|St|Rd|Road|Avenue|Ave|Drive|Dr)\b', re.IGNORECASE)
    matches = pattern.findall(address)
    return matches