"""
QUESTION:
Write a function named `extract_numbers` that takes a string as input, removes all HTML elements from the string, and extracts all numerical values (both integers and decimals) from the remaining string. The function should return a list of the extracted numerical values as strings.
"""

import re
def extract_numbers(input_string):
    # Remove all HTML elements from the string
    input_string = re.sub(r'<.*?>', '', input_string)
    
    # Extract all numerical values from the string and return them in a separate list
    numbers = re.findall(r'\d+\.?\d*', input_string)
    
    return numbers