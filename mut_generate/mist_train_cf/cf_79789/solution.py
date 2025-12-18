"""
QUESTION:
Create a function named `replace_punctuation` that takes a string `s` as input, replaces all punctuation characters with their corresponding ASCII codes in the format "&#ASCII_CODE;", and preserves any whitespace characters. The function should return the modified string.
"""

import string

def replace_punctuation(s):
    output = ""
    for char in s:
        if char in string.punctuation:
            output += "&#" + str(ord(char)) + ";"
        else:
            output += char
    return output