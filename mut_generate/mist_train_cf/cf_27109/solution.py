"""
QUESTION:
Create a Python function `convert_to_snake_case` that takes a single parameter `input_string` (string): A string in camel case with non-alphanumeric characters. The function should return a modified string where the input string is converted to snake case (each word separated by an underscore and all letters are lowercase) and any non-alphanumeric characters are removed except for underscores.
"""

import re

def convert_to_snake_case(input_string):
    # Apply camel to snake case conversion and remove non-alphanumeric characters
    modified_string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', re.sub(r'\W', '', input_string))
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', modified_string).lower()