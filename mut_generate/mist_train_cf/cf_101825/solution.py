"""
QUESTION:
Create a function `extract_numbers` that takes a string as input, removes all HTML elements, and returns a list of all numerical values found in the string. The function should use regular expressions and the `re.findall` method.
"""

import re
def extract_numbers(input_string):
    # Remove all HTML elements from the string
    input_string = re.sub(r'<.*?>', '', input_string)
 
    # Extract all numerical values from the string and return them in a separate list
    numbers = re.findall(r'\d+\.?\d*', input_string)
 
    return numbers