"""
QUESTION:
Write a function `replace_special_and_numbers` that takes a string as input and returns a new string where all special characters and numbers are replaced with their corresponding ASCII values. The function should leave letters (both lowercase and uppercase) unchanged.
"""

import re

def replace_special_and_numbers(string):
    result = ''
    for char in string: 
        if re.match(r'[^a-zA-Z]', char):  # if the character is not a letter
            result += str(ord(char))  # convert it to its ASCII value and append to result string
        else:
            result += char  # append the letter itself
    return result