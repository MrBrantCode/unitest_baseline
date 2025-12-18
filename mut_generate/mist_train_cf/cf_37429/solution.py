"""
QUESTION:
Write a function `parseCopyrightNotice` that takes a copyright notice string as input and returns a dictionary containing the extracted copyright year and the name of the entity. The input string is expected to have a line in the format " * @copyright	Copyright <YEAR> <NAME>." where <YEAR> is a 4-digit number and <NAME> is the entity name. If the input notice is not in the expected format, the function should return an empty dictionary.
"""

import re

def parseCopyrightNotice(notice: str) -> dict:
    pattern = r'@copyright\s+Copyright\s+(\d{4})\s+(.*?)\.'
    match = re.search(pattern, notice)
    if match:
        year = match.group(1)
        name = match.group(2)
        return {'year': year, 'name': name}
    else:
        return {}