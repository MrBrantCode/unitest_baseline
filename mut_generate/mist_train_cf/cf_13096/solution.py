"""
QUESTION:
Write a Python function called `convert_date_format` that takes a string of dates in the format 'dd/mm/yyyy' and returns the string with the dates converted to the format 'mm/dd/yyyy'. The function should use regular expressions and handle strings containing up to 10,000 dates.
"""

import re

def convert_date_format(date_string):
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    substitution = r'\2/\1/\3'
    return re.sub(pattern, substitution, date_string)