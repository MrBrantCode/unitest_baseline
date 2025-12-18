"""
QUESTION:
Create a function called `clean_serial_number` that takes a string as input and returns the string with extra spaces, hyphens, and periods removed or replaced. The function should remove consecutive whitespace characters, hyphens, or periods and replace them with a single space, while preserving the original order of characters and not deleting any valuable information. The function should also remove any leading or trailing spaces from the output.
"""

import re

def clean_serial_number(serial_num):
    return re.sub('[\s.-]+', ' ', serial_num).strip()