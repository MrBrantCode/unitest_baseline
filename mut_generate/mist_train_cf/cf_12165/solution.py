"""
QUESTION:
Create a function `contains_consecutively` that takes two strings as arguments and returns `True` if the first string contains the second string consecutively, ignoring case and non-alphanumeric characters, and `False` otherwise.
"""

import re

def contains_consecutively(string1, string2):
    # Remove non-alphanumeric characters and convert to lowercase
    string1 = re.sub('[^a-zA-Z0-9]', '', string1).lower()
    string2 = re.sub('[^a-zA-Z0-9]', '', string2).lower()
    
    # Check if the second string appears consecutively in the first string
    return string2 in string1