"""
QUESTION:
Develop a function `find_street` that takes a string representing a residential or business location as input and returns the street moniker contained within the string. The function should use a regular expression pattern to identify the street moniker, which is assumed to be a sequence of one or more words that come after a number in the input string. If a street moniker is found, the function should return it as a string; otherwise, it should return "Street not found".
"""

import re

def find_street(address):
    match = re.search(r'\d+\s([\w\s]+)', address)
    if match:
        return match.group(1)
    else:
        return "Street not found"