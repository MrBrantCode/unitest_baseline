"""
QUESTION:
Write a function `convert_date_format` that takes a string containing dates in the format 'dd/mm/yyyy' and returns a string with all dates converted to the format 'mm/dd/yyyy'. The function should handle strings with up to 10,000 dates.
"""

import re

def convert_date_format(input_string):
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    substitution = r'\2/\1/\3'
    output_string = re.sub(pattern, substitution, input_string)
    return output_string