"""
QUESTION:
Write a function `extract_info` to extract the full name, date of birth (in the format DD/MM/YYYY), residential address, and Social Security Number (in the format XXX-XX-XXXX) from a provided text string. The function should return a dictionary containing the extracted information if the input string matches the specified format, otherwise return "Not found".
"""

import re

def extract_info(s):
    pattern = re.compile(r'(?P<name>[\w\s]+);\s'
                         r'(?P<dob>[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]);\s'
                         r'(?P<address>[\w\s,]+);\s'
                         r'(?P<ssn>[0-9]{3}-[0-9]{2}-[0-9]{4})'
                         )
    match = pattern.search(s)
    if match:
        return match.groupdict()
    else:
        return "Not found"