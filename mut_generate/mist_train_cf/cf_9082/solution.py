"""
QUESTION:
Write a function `preprocess_string` that takes a string as input and returns the string after removing all whitespace and punctuation and converting all characters to lowercase.
"""

import string

def preprocess_string(input_string):
    # Remove whitespace and punctuation
    input_string = input_string.translate(str.maketrans('', '', string.whitespace + string.punctuation))
    
    # Convert characters to lowercase
    input_string = input_string.lower()
    
    return input_string