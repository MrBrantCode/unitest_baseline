"""
QUESTION:
Create a function named `extract_alphabets` that takes a string as input and returns the string with all non-alphabetic characters removed, except for whitespaces.
"""

import re

def extract_alphabets(input_string):
    return re.sub('[^A-Za-z ]+', '', input_string)