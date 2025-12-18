"""
QUESTION:
Construct a function `convert_string` that takes a string as an argument and replaces all non-alphanumeric characters (excluding spaces) with "%".
"""

def convert_string(inputString):
    result = ""
    for char in inputString:
        if char.isalnum() or char == " ":
            result += char
        else:
            result += "%"
    return result