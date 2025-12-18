"""
QUESTION:
Create a function called `tokenize_string` that takes a string as input and returns a list of tokens. Tokens are separated by spaces, can be alphanumeric strings (but cannot start with a digit), and can include special characters '.', ',', '!', '?' as part of a larger token. The function should not allow standalone special characters.
"""

import re

def tokenize_string(input_string):
    # Using regular expression to tokenize the input string
    tokens = re.findall(r'[a-zA-Z_][\w.,!?]*|[\w][\w.,!?]*[.,!?]', input_string)
    return tokens