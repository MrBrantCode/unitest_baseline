"""
QUESTION:
Create a function named `contains_consecutively` that takes two strings as arguments. The function should be case insensitive and only consider alphanumeric characters when comparing the strings. It should return True if the second string appears consecutively in the first string, and False otherwise.
"""

import re

def contains_consecutively(string1, string2):
    # Remove non-alphanumeric characters and convert to lowercase
    string1 = re.sub('[^a-zA-Z0-9]', '', string1).lower()
    string2 = re.sub('[^a-zA-Z0-9]', '', string2).lower()
    
    # Check if the second string appears consecutively in the first string
    return string2 in string1