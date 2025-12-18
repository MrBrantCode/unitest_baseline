"""
QUESTION:
Write a function `classify_string(string)` that classifies a given string into one of four categories using Regular Expressions: 
- Alphabetic strings (only contains alphabets)
- Numeric strings (only contains numbers)
- Alphanumeric strings (contains both alphabets and numbers)
- Special character strings (only contains special characters and no spaces)

The function should return a string indicating the category of the input string. If the string does not fit into any of these categories, return "Unknown".
"""

import re

def classify_string(string):
    # Check for alphabetic string
    if re.match(r'^[A-Za-z]+$', string):
        return "Alphabetic string"
    
    # Check for numeric string
    if re.match(r'^[0-9]+$', string):
        return "Numeric string"
    
    # Check for alphanumeric string
    if re.match(r'^[A-Za-z0-9]+$', string):
        return "Alphanumeric string"
    
    # Check for special character string
    if re.match(r'^[^A-Za-z0-9\s]+$', string):
        return "Special character string"
    
    # If none of the above categories match, return unknown
    return "Unknown"