"""
QUESTION:
Write a function called `convert_to_camel_case` that takes a string as input and returns the string converted to CamelCase. The function should handle strings of any length, with leading and trailing spaces, multiple consecutive spaces, special characters, and numbers, and should not use any built-in functions or libraries for conversion. The runtime complexity should be efficient, i.e., O(n), where n is the length of the input string.
"""

def convert_to_camel_case(string):
    string = string.strip()
    result = ''
    capitalize_next = False

    for char in string:
        if char == ' ':
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char

    return result