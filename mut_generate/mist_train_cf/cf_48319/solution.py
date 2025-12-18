"""
QUESTION:
Create a function called `checkCamelCasePalindrome` that takes a string as input and returns a boolean indicating whether the string in camelCase form is a palindrome or not. The function should handle special characters and numbers by removing them from the string. The function should also be optimized for large inputs, with a time complexity of O(n), where n is the length of the string.
"""

import re

def checkCamelCasePalindrome(s):
    s = re.sub(r"[\W_]+", "", s) # Remove special characters and underscores
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s) 
    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
    s = ''.join(x.capitalize() or '_' for x in s.split('_')) 
    s = s.replace("_", "") # remove underscores before checking for palindrome
    return s == s[::-1]