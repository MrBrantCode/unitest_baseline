"""
QUESTION:
Create a function named `modify` that takes a string of alphanumeric symbols as input, and returns a modified version of the string where each character immediately following an underscore is converted to its uppercase equivalent.
"""

def modify(text):
    result = ''
    capitalize_next = False
    for char in text:
        if char == '_':
            result += char
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char

    return result