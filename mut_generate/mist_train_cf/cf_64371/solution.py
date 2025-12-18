"""
QUESTION:
Create a custom function named `custom_concat` that takes two alphanumeric strings as input parameters and returns a new string that is the concatenation of the input strings. The function should not use the default string concatenation methods, instead implementing its own logic to combine the strings. The function should work with any alphanumeric strings, not just specific examples.
"""

def custom_concat(str1, str2):
    result = ''
    for character in str1:
        result += character
    for character in str2:
        result += character
    return result