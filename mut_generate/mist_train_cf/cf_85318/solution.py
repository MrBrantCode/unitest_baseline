"""
QUESTION:
Write a function named `remove_special_characters` that takes a string as input and returns the string with all special characters removed, except for spaces. The function should be able to handle strings containing alphanumeric characters, spaces, and special characters.
"""

import re

def remove_special_characters(s):
    return re.sub('[^A-Za-z0-9 ]+', '', s)