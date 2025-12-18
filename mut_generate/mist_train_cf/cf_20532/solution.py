"""
QUESTION:
Create a function `extract_phone_numbers(text)` that takes a string `text` as input and returns a list of phone numbers in the order they appear in the string. The function should extract phone numbers in two formats: (XXX) XXX-XXXX and +XXX-XXXXXXXXXX, but ignore any phone numbers with the area code "555".
"""

import re

def extract_phone_numbers(text):
    phone_numbers = []
    pattern = r"\((\d{3})\) (\d{3})-(\d{4})|\+(\d{1,3})-(\d{10})"
    matches = re.findall(pattern, text)
    
    for match in matches:
        if match[0] != "555" and match[3] != "555":
            if match[0] != "":
                phone_numbers.append(f"({match[0]}) {match[1]}-{match[2]}")
            else:
                phone_numbers.append(f"+{match[3]}-{match[4]}")
    
    return phone_numbers