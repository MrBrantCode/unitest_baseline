"""
QUESTION:
Create a function `insert_spaces(input_string)` that inserts a space before each word that commences with an uppercase letter in the given `input_string`. The function should not insert a space at the beginning of the string if it starts with an uppercase letter. Non-alphanumeric characters should be treated as part of the preceding word.
"""

import re

def insert_spaces(input_string):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", input_string)