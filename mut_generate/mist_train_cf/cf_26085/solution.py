"""
QUESTION:
Create a regular expression pattern that can extract the first name, last name, and age from a given string, assuming the string is in the format "first_name,last_name,age" where 'first_name' and 'last_name' are alphabetic and 'age' is numeric. The function should be able to handle strings of varying lengths and the age can be any positive number.
"""

import re

def extract_info(input_string):
    pattern = r"([a-zA-Z]+),([a-zA-Z]+),(\d+)"
    match = re.match(pattern, input_string)
    if match:
        return match.groups()
    else:
        return None