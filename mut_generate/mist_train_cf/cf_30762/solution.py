"""
QUESTION:
Create a function `parse_license_conditions(license_text: str) -> List[str]` that takes a string `license_text` representing a software license text, extracts the conditions specified in the license, and returns a list of the extracted conditions. The `license_text` contains numbered points followed by a period and space, with each point on a new line, and the length of `license_text` is between 1 and 1000 characters.
"""

from typing import List

def parse_license_conditions(license_text: str) -> List[str]:
    conditions = []
    lines = license_text.split('\n')
    for line in lines:
        if line.strip().startswith('#'):
            condition = line.split('. ')[1].strip()
            conditions.append(condition)
    return conditions