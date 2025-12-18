"""
QUESTION:
Create a function `extract_numbers` that takes an input string as an argument. The function should use regular expressions to extract all numerical values from the string and return them in a separate list. The function should also remove all HTML elements from the string before extracting the numerical values.
"""

import re

def extract_numbers(input_string):
    # Remove all HTML elements from the string
    input_string = re.sub(r'<.*?>', '', input_string)
    
    # Extract all numerical values from the string and return them in a separate list
    numbers = re.findall(r'\d+\.?\d*', input_string)
    
    return numbers