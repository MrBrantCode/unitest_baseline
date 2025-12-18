"""
QUESTION:
Implement a function called `extract_and_transform` that takes a string `input_str` as input. The function should extract a substring enclosed within square brackets `[]`, remove any non-numeric characters from the extracted substring, and return the resulting numeric string as an integer. If the extracted substring is empty or does not contain any numeric characters, return 0.
"""

import re

def extract_and_transform(input_str):
    match = re.search(r'\[(.*?)\]', input_str)
    if match:
        extracted = match.group(1)
        num_value = ''.join(filter(str.isdigit, extracted))
        return int(num_value) if num_value else 0
    else:
        return 0