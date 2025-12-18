"""
QUESTION:
Create a function `find_pattern(string)` that takes a string as input and returns the first occurrence of a specific pattern if found, or 'No match found' otherwise. The pattern consists of exactly three uppercase letters followed by two lowercase letters, immediately followed by three digits, a special symbol, and two uppercase letters.
"""

import re

def find_pattern(string):
    pattern = r'[A-Z]{3}[a-z]{2}\d{3}[\W][A-Z]{2}'
    match = re.search(pattern, string)
    
    if match:
        return match.group(0)
    else:
        return 'No match found'