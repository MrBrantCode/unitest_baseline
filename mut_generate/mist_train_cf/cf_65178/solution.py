"""
QUESTION:
Create a function named `convert` that takes a string as input and returns the string with all alphabetic characters converted to upper-case and all numbers converted to their binary representation. The function should leave all non-alphabetic and non-numeric characters unchanged.
"""

def convert(input_str):
    output = ""
    for char in input_str:
        if char.isalpha():
            output += char.upper()
        elif char.isdigit():
            output += bin(int(char))[2:]
        else:
            output += char
    return output